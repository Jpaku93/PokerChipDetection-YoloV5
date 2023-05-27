# PokerChip Detection YoloV5

 ### The Problem:
 The original idea is to count or track the number of chips assigned to a player, Reasons for a system would lead to tracking fraud chips, data collection and analysis of player behaviour and automatic chip counting systems using a mix of computer vision, count of chips on the table and per person.
 <br/>
 Research reference: https://patents.google.com/patent/US5781647A/en

 ### Data Collection and Preparation: 
 Images are collected from youtube video and image urls.  <br />
 From the image file the data is anottated using labelImg repo. <br />
 The annotations are stored into yolo format .txt file for each corresponding image, then organised into a dataset folder containing train and valid files with seperate annotation and image files. <br />   

 ### Framework:
Tensorflow <br /> 
YoloV5 <br />

 ### Model Development: 


 ### Training: 
 training is performed at 130 epochs. <br />
 training 130 epochs with 300 images took about an hour<br />
 30 epochs test runs <br />
 No specific reason for 130 epochs besides making sure there was enough training  <br />

## Evaluation:

## Overview:
The object detection model (YoloV5) performs extremely well. After a 4 or 5 iterations of training the model detects most cases of poker chips <br /><br />

The first model identified more false positives than positives at a threshold of 70 with 30 epochs training, after succesfully increasing the epochs and threshold the model struggled to identify a majority of poker chips so another iteration of training data was annotated. <br /><br />

Within the next few trials were attempts to identify multiple labels for poker chips such as stack of chips, bundle of chips and single chip but too many false positives appeared. The final model was trained on overall pokerchips, single bundle, stacks and piles. <br /><br />

Overall the final model is not the optimal output but performs well to identify the majority of the chips from certain angles and different colors. <br />

## Dependencies: 


## Installation Instructions: 

## Usage Guide: 

## Configuration: 

## Continuous Improvement: 