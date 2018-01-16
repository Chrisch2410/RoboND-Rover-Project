
[![Udacity - Robotics NanoDegree Program](https://s3-us-west-1.amazonaws.com/udacity-robotics/Extra+Images/RoboND_flag.png)](https://www.udacity.com/robotics)
# Project 1: Search and Sample Return
## Writeup by Muthanna A.Attyah
## Jan 2018

## [Rubric](https://review.udacity.com/#!/rubrics/916/view) Points

<p align="center"> <img src="./misc/rover_image.jpg"> </p>

## 1. Project Environment Preparation:

Please note that I have used the following environment to test/run the project:

* Operating System: **Ubuntu 16.04 LTS kernel 4.4.0-109-generic**
* Unity Simulator: **Roversim.x86_64**
* Unity Simulator Screen Resolution: **1024 x 640**
* Unity Simulator Graphics Quality: **Fantastic**
* Test Video recording FPS: **60 FPS**
* drive_rover.py FPS: **16-18 FPS**
* Anaconda: **Version 4.4.7**
* RoboND Anaconda Environment

**Note:** running the simulator with different choices of resolution and graphics quality may produce different results, particularly on different machines!  

## 2. Recording data in Training Mode

After getting the above mentioned environment components downloaded and installed, I have started reordering data from Rover Simulator in "Training Mode" using same resolution mentioned above. Recorded date was saved in two new folders "rec1_dataset" and "rec2_dataset" which will be used in addition to the already provided "test_dataset".

"rec1_dataset" is a short recording covering 28% of ground and I used it for rapid testing to fine tune image processing function. "rec2_dataset" is a long recording covering 100% of ground map and I used it to verify the final mapping and fidelity of image processing function before exporting it to perception.py script and testing it in autonomous mode.

## 4. Project Jupyter Notebook Analysis

Jupyter notebook was used to go through the full image processing pipeline starting from image aquestion until final navigation and mapping output.

### 4.1 Used Python Libraries

Following python libraries was used as part of notebook analysis:

* **numpy**: for array maths, image can be treated as array of numbers and modified using numpy.
* **matplotlib.pyplot**: to plot results in a very fancy figures and save them as images for this report.
* **matplotlib.image**: to read images from files.
* **cv2**: OpenCV for perspective transform.
* **glob**: to read in a list of images from a folder.
* **pandas**: to read a CSV file into a dataframe
* **imageio**: to read images and video.

## 4.2 Image Processing Pipeline

From a highlevel, the image processing pipeline that will be required to process images aquired from the rover camera in order to:

* Produce rover driving angle.
* Detect any golden rocks in the way 
* Update World Map to show Navigation map

can be summrized as shown in below diagram.

<p align="center"> <img src="./misc/pipeline.jpg"> </p>

In the next sections I will discuss each stage function in the pipeline and show sample outputs from each.

## 4.3 Perspective Transform Function

First function in the pipeline is the perspective trnasform function which will convert image seen by the rover camera into a top-view image that will be used to map the navigable area, obistcale area, and golden rocks. Transformation calculation is done with help of the provided calibration grid image. coordinates of the grid square that is directly in front of the rover camera is taken as source:

```python
src = np.float32([
                 [14, 140],      # Left Bottom
                 [301 ,140],     # Right Bottom
                 [200, 96],      # Right Top
                 [118, 96]       # Left Top
                 ])              # above data captured from grid calibration image.
```

then one sequare in a top view map is taken as destination, adding 6 pixels to account for the unvisible distance from the rover edge to the 1st visible point.

```python
hs_size = 10/2             # half the size of one square
b_ofst  = 6                # bottom offset to account for distance from rover edge to 1st camera visible point
x_cntr  = grid_img.shape[1]/2 # center of the image x axis
y_end   = grid_img.shape[0]   # end of y or bottom of image

dst = np.float32([
                 [x_cntr - hs_size, y_end - b_ofst],             # Left Bottom
                 [x_cntr + hs_size, y_end - b_ofst],             # Right Bottom
                 [x_cntr + hs_size, y_end - 2*hs_size - b_ofst], # Right Top
                 [x_cntr - hs_size, y_end - 2*hs_size - b_ofst], # Left Top
                 ])
```
Using OpenCV function 'cv2.warpPerspective()' we can now transform the prespective of aquired image from camera view into top-view.

```python
def perspect_transform(img, src, dst):

    M = cv2.getPerspectiveTransform(src, dst)  # Get transform matrix using src and dst boxes
    warped = cv2.warpPerspective(img,          # Warp image keep same size as input image 
                                 M, 
                                 (img.shape[1], img.shape[0]))
```

Below are outputs for navigable and rock sample images:

<p align="center"> <img src="./output/warp_fun.jpg"> </p>

## 4.4 Color Threshold Function

Next stage is the color thresholding function that will be required to identify the navigable, obistcale, and golden rock areas. Doing color thresholding on image before prespective transform or after the prespective transform will give the same results. So order is these two stages does not matter.

For navigable/obsticale thresholding I used RGB numbers as advised in the project template since it was working fine and I have tried values other then 'rgb_thr=(160,160,160)' but reverted back later becuase I did not get any improved results in detection of navigable area.

```python
def navi_thresh(img):

    # Threshold of RGB > 160 does a nice job of identifying ground pixels only
    rgb_thr=(160,160,160)
     
    # mask will contain a boolean array with "True" for each pixel above threshold
    mask = (img[:,:,0] > rgb_thr[0]) \
         & (img[:,:,1] > rgb_thr[1]) \
         & (img[:,:,2] > rgb_thr[2])

    # Create an array of zeros same xy size as img, but single channel
    # Index the array with the mask and set to 1
    navi = np.zeros_like(img[:,:,0])
    navi[mask] = 1
    
    navi[:int(img.shape[0]*.5),:]=0 # clip upper 50% of image to improve fidelity
    
    # Create an array of ones same xy size as img, but single channel
    # Index the array with the mask and set to 0
    obst = np.ones_like(img[:,:,0])
    obst[mask] = 0
    
    obst[:int(img.shape[0]*.5),:]=1 # clip upper 50% of image to improve fidelity
    
    return navi,obst                        # Return both images

```

<p align="center"> <img src="./output/thresh_fun.jpg"> </p>

## 4.5 Transform and Color Thresholding of Sample Image

<p align="center"> <img src="./output/threshwarp_fun.jpg"> </p>

## 4.6 Rover Centric Coordinates Functions

<p align="center"> <img src="./output/rover_coords.jpg"> </p>

## 4.7 World Map Image
<p align="center"> <img src="./output/world_space.jpg"> </p>

## 4.8 Ground Truth Map

<p align="center"> <img src="./output/ground_truth.jpg"> </p>

## 4.9 Image Processing Function

Populate the `process_image()` function with the appropriate analysis steps to map pixels identifying navigable terrain, obstacles and rock samples into a worldmap.  Run `process_image()` on your test data using the `moviepy` functions provided to create video output of your result. 
And another! 

<p align="center"> <img src="./output/test_frame.jpg"> </p>

## 4.10 Producing a Video to test image processing pipeline

The final testing video after implementing all above mentioned steps is uploaded on YouTube on the following link:

[![test video](http://img.youtube.com/vi/3z5Nvw0yioA/default.jpg)](http://www.youtube.com/watch?v=3z5Nvw0yioA)

as you can see in the video after covering more than 99.4% of the ground; fidelity was 56.5% which is acceptable for this test but it can be much further improved.

## 5. Exporting Image Processing function to perception.py script
Fill in the `perception_step()` (at the bottom of the `perception.py` script) and `decision_step()` (in `decision.py`) functions in the autonomous mapping scripts and an explanation is provided in the writeup of how and why these functions were modified as they were.

## 6. Running **Autonomous Navigation/Mapping**

Launching in autonomous mode your rover can navigate and map autonomously.  
Explain your results and how you might improve them in your writeup.  

* Fill in the `perception_step()` function within the `perception.py` script with the appropriate image processing functions to create a map and update `Rover()` data (similar to what you did with `process_image()` in the notebook). 
* Fill in the `decision_step()` function within the `decision.py` script with conditional statements that take into consideration the outputs of the `perception_step()` in deciding how to issue throttle, brake and steering commands. 
* Iterate on your perception and decision function until your rover does a reasonable (need to define metric) job of navigating and mapping.  


## 7. Future improvments.
Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  


