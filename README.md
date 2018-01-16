## Project: Search and Sample Return
### Writeup by Muthanna A.Attyah
### Jan 2018
<p align="center"> <img src="./output/rover_image.jpg"> </p>

## 1. Project Environment Preparation:

Please note that I have used the following environment to test/run the project:

* Operating System: **Ubuntu 16.04 LTS kernel 4.4.0-109-generic**
* Unity Simulator: **Roversim.x86_64**
* Unity Simulator Screen Resolution: **1024 x 640**
* Unity Simulator Graphics Quality: **Fantastic**
* Anaconda: **Version 4.4.7**
* RoboND Anaconda Environment

## 2. Recording data in Training Mode

After getting the above mentioned enviroment components downloaded and installed, I have started recordering data from Rover Simulator in "Training Mode" using same resolution mentioned above. Recorded date was saved in two new folders "rec1_dataset" and "rec2_dataset" which will be used in additon to the already provided "test_dataset".
"rec1_dataset" is a short recording covering 28% of ground and I used it for rapid testing to fine tune image processing function. "rec2_dataset" is a long recording covering 100% of ground map and I used it to verify the final maping and fidelity of image processing function before exporting it to perception.py script and testing it in autonomous mode.


## 3. Image Processing Pipeline

## 4. Transform Function

<p align="center"> <img src="./output/warp_fun.jpg"> </p>

## 5. Color Threshold Function

<p align="center"> <img src="./output/thresh_fun.jpg"> </p>

## 6. Transform and Color Thresholding of Sample Image

<p align="center"> <img src="./output/threshwarp_fun.jpg"> </p>

## 7. Rover Centric Coordinates Functions

<p align="center"> <img src="./output/rover_coords.jpg"> </p>

## 8. World Map Image
<p align="center"> <img src="./output/world_space.jpg"> </p>

## 9. Ground Truth Map

<p align="center"> <img src="./output/ground_truth.jpg"> </p>

## 10. Image Processing Function

<p align="center"> <img src="./output/test_frame.jpg"> </p>

## 11. Producing a Video to test image processing pipeline

## 12. Exporting Image Processing function to perception.py script

## 13. Running **Autonomous Navigation/Mapping**


* Fill in the `perception_step()` function within the `perception.py` script with the appropriate image processing functions to create a map and update `Rover()` data (similar to what you did with `process_image()` in the notebook). 
* Fill in the `decision_step()` function within the `decision.py` script with conditional statements that take into consideration the outputs of the `perception_step()` in deciding how to issue throttle, brake and steering commands. 
* Iterate on your perception and decision function until your rover does a reasonable (need to define metric) job of navigating and mapping.  


## 13. Future improvments.

## [Rubric](https://review.udacity.com/#!/rubrics/916/view) Points
### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Notebook Analysis
#### 1. Run the functions provided in the notebook on test images (first with the test data provided, next on data you have recorded). Add/modify functions to allow for color selection of obstacles and rock samples.
Here is an example of how to include an image in your writeup.

#### 1. Populate the `process_image()` function with the appropriate analysis steps to map pixels identifying navigable terrain, obstacles and rock samples into a worldmap.  Run `process_image()` on your test data using the `moviepy` functions provided to create video output of your result. 
And another! 

### Autonomous Navigation and Mapping

#### 1. Fill in the `perception_step()` (at the bottom of the `perception.py` script) and `decision_step()` (in `decision.py`) functions in the autonomous mapping scripts and an explanation is provided in the writeup of how and why these functions were modified as they were.


#### 2. Launching in autonomous mode your rover can navigate and map autonomously.  Explain your results and how you might improve them in your writeup.  

**Note: running the simulator with different choices of resolution and graphics quality may produce different results, particularly on different machines!  Make a note of your simulator settings (resolution and graphics quality set on launch) and frames per second (FPS output to terminal by `drive_rover.py`) in your writeup when you submit the project so your reviewer can reproduce your results.**

Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  


