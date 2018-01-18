import numpy as np
import cv2


# Define a function to threshold warped image and show navigable/obstacles areas
def navi_thresh(img):

    obst_lower = (0,0,0)    # RGB lower limit for obstacle area
    obst_upper = (70,80,120)  # RGB upper limit for obstacle area    
    
    # sky color is between obst and navi ranges (70,80,120) to (160,160,160)
    
    navi_lower = (160,160,160)  # RGB lower limit for naviagble area
    navi_upper = (255,255,255)  # RGB upper limit for naviagble area
        
    navi_t = cv2.inRange(img, navi_lower, navi_upper) #
    obst_t = cv2.inRange(img, obst_lower, obst_upper)
     
    navi_t[:int(img.shape[0]*.5),:]=0 # clip upper 50% of image to improve fidelity
    # obst_t[:int(img.shape[0]*.5),:]=1 # clip upper 50% of image to improve fidelity
    
    return navi_t*255,obst_t*255    # Return both images


# Define a function to threshold rock calibration image and isolate the rock.
def rock_thresh(img):
    
    hsv_img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    rock_lower = np.array([0,200,100])     # HSV lower limit for golden rocks
    rock_upper = np.array([179,255,255])   # HSV upper limit for golden rocks
    
    rock_t = cv2.inRange(hsv_img, rock_lower, rock_upper)
      
    return rock_t*255

# Define a function to convert from image coords to rover coords
def rover_coords(binary_img):
    # Identify nonzero pixels
    ypos, xpos = binary_img.nonzero()
    # Calculate pixel positions with reference to the rover position being at the 
    # center bottom of the image.  
    x_pixel = -(ypos - binary_img.shape[0]).astype(np.float)
    y_pixel = -(xpos - binary_img.shape[1]/2 ).astype(np.float)
    return x_pixel, y_pixel


# Define a function to convert to radial coords in rover space
def to_polar_coords(x_pixel, y_pixel):
    # Convert (x_pixel, y_pixel) to (distance, angle) 
    # in polar coordinates in rover space
    # Calculate distance to each pixel
    dist = np.sqrt(x_pixel**2 + y_pixel**2)
    # Calculate angle away from vertical for each pixel
    angles = np.arctan2(y_pixel, x_pixel)
    return dist, angles

# Define a function to map rover space pixels to world space
def rotate_pix(xpix, ypix, yaw):
    # Convert yaw to radians
    yaw_rad = yaw * np.pi / 180
    xpix_rotated = (xpix * np.cos(yaw_rad)) - (ypix * np.sin(yaw_rad))
                            
    ypix_rotated = (xpix * np.sin(yaw_rad)) + (ypix * np.cos(yaw_rad))
    # Return the result  
    return xpix_rotated, ypix_rotated

def translate_pix(xpix_rot, ypix_rot, xpos, ypos, scale): 
    # Apply a scaling and a translation
    xpix_translated = (xpix_rot / scale) + xpos
    ypix_translated = (ypix_rot / scale) + ypos
    # Return the result  
    return xpix_translated, ypix_translated


# Define a function to apply rotation and translation (and clipping)
# Once you define the two functions above this function should work
def pix_to_world(xpix, ypix, xpos, ypos, yaw, world_size, scale):
    # Apply rotation
    xpix_rot, ypix_rot = rotate_pix(xpix, ypix, yaw)
    # Apply translation
    xpix_tran, ypix_tran = translate_pix(xpix_rot, ypix_rot, xpos, ypos, scale)
    # Perform rotation, translation and clipping all at once
    x_pix_world = np.clip(np.int_(xpix_tran), 0, world_size - 1)
    y_pix_world = np.clip(np.int_(ypix_tran), 0, world_size - 1)
    # Return the result
    return x_pix_world, y_pix_world

# Define a function to perform a perspective transform
def perspect_transform(img, src, dst):
           
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))# keep same size as input image
    
    return warped


# Apply the above functions in succession and update the Rover state accordingly
def perception_step(Rover):
    # Perform perception steps to update Rover()
    
    # 1) Define source and destination points for perspective transform
    #------------------------------------------------------------------
    
    scale    = 10             # each 10x10 pixel square represents 1 square meter
    hs_size  = scale/2        # half the size of one square
    b_ofst   = 6              # bottom offset to account for distance from rover edge to 1st camera visiable point
    
    rvr_xpos = Rover.pos[0]
    rvr_ypos = Rover.pos[1]
    rvr_yaw  = Rover.yaw
    
    x_cntr   = Rover.img.shape[1]/2 # center of the image x axis
    y_end    = Rover.img.shape[0]   # end of y or bottom of image
    wrl_shp0 = Rover.worldmap.shape[0]
    
    
    src = np.float32([
                     [14, 140],      # Left Bottom
                     [301 ,140],     # Right Bottom
                     [200, 96],      # Right Top
                     [118, 96]       # Left Top
                     ])              # above data captured from grid calibration image.

    dst = np.float32([
                     [x_cntr - hs_size, y_end - b_ofst],             # Left Bottom
                     [x_cntr + hs_size, y_end - b_ofst],             # Right Bottom
                     [x_cntr + hs_size, y_end - 2*hs_size - b_ofst], # Right Top
                     [x_cntr - hs_size, y_end - 2*hs_size - b_ofst], # Left Top
                     ])
    
    # 2) Apply perspective transform
    #------------------------------------------------------------------

    img_wrpd = perspect_transform(Rover.img, src, dst) #warp the image
    
    
    # 3) Apply color threshold to identify navigable terrain/obstacles/rock samples
    #------------------------------------------------------------------
    navi_thr,obst_thr = navi_thresh(img_wrpd)  # Threshold warped image to show both navigable and obstcales areas
    rock_thr = rock_thresh(img_wrpd)           # Threshold calibration image to isolate the rock
    
    # 4) Update Rover.vision_image (this will be displayed on left side of screen)
    #------------------------------------------------------------------
    Rover.vision_image[:,:,0] = obst_thr*255 # obstacle color-thresholded binary image
    Rover.vision_image[:,:,1] = rock_thr*255 # rock_sample color-thresholded binary image
    Rover.vision_image[:,:,2] = navi_thr*255 # navigable terrain color-thresholded binary image
    

    # 5) Convert map image pixel values to rover-centric coords
    #------------------------------------------------------------------
    navix_pix, naviy_pix = rover_coords(navi_thr)  # convert navigable area thresholded to rover coords.
    obstx_pix, obsty_pix = rover_coords(obst_thr)  # convert obstacle area thresholded to rover coords.
    rockx_pix, rocky_pix = rover_coords(rock_thr)  # convert rock thresholded to rover coords.
    
    # 6) Convert rover-centric pixel values to world coordinates
    #------------------------------------------------------------------
    naviy_wld, navix_wld = pix_to_world(navix_pix, naviy_pix,          # convert navigable area
                                        rvr_xpos, rvr_ypos, rvr_yaw,
                                        wrl_shp0,scale)
    
    obsty_wld, obstx_wld = pix_to_world(obstx_pix, obsty_pix,          # convert obsticale area
                                        rvr_xpos, rvr_ypos, rvr_yaw,
                                        wrl_shp0,scale)
    
    rocky_wld, rockx_wld = pix_to_world(rockx_pix, rocky_pix,          # convert rock area
                                        rvr_xpos, rvr_ypos, rvr_yaw,
                                        wrl_shp0,scale)
    
    # 7) Update Rover worldmap (to be displayed on right side of screen)
    #------------------------------------------------------------------
    Rover.worldmap[obstx_wld, obsty_wld, 0] = 255  # set obsticale area pixels to RED
    Rover.worldmap[navix_wld, naviy_wld, 2] = 255  # set navigable area pixels to BLUE
    Rover.worldmap[rockx_wld, rocky_wld, :] = 255  # set rock area to WHITE

    # 8) Convert rover-centric pixel positions to polar coordinates
    #------------------------------------------------------------------
    xpix, ypix = rover_coords(navi_thr)
    rock_xpix, rock_ypix = rover_coords(rock_thr)
    
    # Update Rover pixel distances and angles   
    Rover.nav_dists, Rover.nav_angles = to_polar_coords(xpix, ypix)
    Rover.rock_nav_dists, Rover.rock_nav_angles = to_polar_coords(rock_xpix, rock_ypix)
    
    return Rover