[//]: # (Image References)

[image1]: ../misc/rover_image.jpg
[image2]: ../output/sample_img.jpg
[image3]: ../output/grid_img.jpg
[image4]: ../output/rock_img.jpg
[image5]: ../output/navi_w.jpg
[image6]: ../output/rock_w.jpg
[image7]: ../output/navi_t.jpg
[image8]: ../output/obst_t.jpg
[image9]: ../output/rock_t.jpg
[image10]: ../output/navi_wt.jpg
[image11]: ../output/obst_wt.jpg
[image12]: ../output/rock_wt.jpg
[image13]: ../output/map_img.jpg
[image14]: ../output/navi_rc.jpg
[image15]: ../output/tst_frame.jpg

## Project: Search and Sample Return
![alt text][image1]
### Writeup by Muthanna A.Attyah
### Jan 2018

##1. Project Environment Preparation:

Please note that I have used the following environment to test/run the project:

* Operating System: Ubuntu 16.04 LTS kernel 4.4.0-109-generic
* Unity Simulator: Roversim.x86_64 
* Unity Simulator Screen Resolution: 1024 x 640
* Unity Simulator Graphics Quality: Fantastic
* Anaconda: Version 4.4.7
* RoboND anaconda environment

##2. Recording data in "Training Mode"

After getting the above mentioned enviroment components downloaded and installed, I have started recordering data from Rover Simulator in "Training Mode". in additon to the already provided "test_dataset" I have recorded in two new sets in two new folders "rec1_dataset" and "rec2_dataset". 

"rec1_dataset" is a short recording I used it for rapid testing and change of fucntions. "rec2_dataset" is a long recording covering the full ground map and I used it to verify the final maping and fidelity of my functions before testing in autonomous mode.


---


**The goals / steps of this project are the following:**  

**Training / Calibration**  

* Download the simulator and take data in "Training Mode"
* Test out the functions in the Jupyter Notebook provided
* Add functions to detect obstacles and samples of interest (golden rocks)
* Fill in the `process_image()` function with the appropriate image processing steps (perspective transform, color threshold etc.) to get from raw images to a map.  The `output_image` you create in this step should demonstrate that your mapping pipeline works.
* Use `moviepy` to process the images in your saved dataset with the `process_image()` function.  Include the video you produce as part of your submission.

**Autonomous Navigation / Mapping**

* Fill in the `perception_step()` function within the `perception.py` script with the appropriate image processing functions to create a map and update `Rover()` data (similar to what you did with `process_image()` in the notebook). 
* Fill in the `decision_step()` function within the `decision.py` script with conditional statements that take into consideration the outputs of the `perception_step()` in deciding how to issue throttle, brake and steering commands. 
* Iterate on your perception and decision function until your rover does a reasonable (need to define metric) job of navigating and mapping.  



## [Rubric](https://review.udacity.com/#!/rubrics/916/view) Points
### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  



![alt text][image2]
![alt text][image3]
![alt text][image4]
![alt text][image5]
![alt text][image6]
![alt text][image7]
![alt text][image8]
![alt text][image9]
![alt text][image10]
![alt text][image11]
![alt text][image12]
![alt text][image13]
![alt text][image14]
![alt text][image15]

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  

You're reading it!

### Notebook Analysis
#### 1. Run the functions provided in the notebook on test images (first with the test data provided, next on data you have recorded). Add/modify functions to allow for color selection of obstacles and rock samples.
Here is an example of how to include an image in your writeup.

![alt text][image1]

#### 1. Populate the `process_image()` function with the appropriate analysis steps to map pixels identifying navigable terrain, obstacles and rock samples into a worldmap.  Run `process_image()` on your test data using the `moviepy` functions provided to create video output of your result. 
And another! 

![alt text][image2]
### Autonomous Navigation and Mapping

#### 1. Fill in the `perception_step()` (at the bottom of the `perception.py` script) and `decision_step()` (in `decision.py`) functions in the autonomous mapping scripts and an explanation is provided in the writeup of how and why these functions were modified as they were.


#### 2. Launching in autonomous mode your rover can navigate and map autonomously.  Explain your results and how you might improve them in your writeup.  

**Note: running the simulator with different choices of resolution and graphics quality may produce different results, particularly on different machines!  Make a note of your simulator settings (resolution and graphics quality set on launch) and frames per second (FPS output to terminal by `drive_rover.py`) in your writeup when you submit the project so your reviewer can reproduce your results.**

Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  



![alt text][image3]


