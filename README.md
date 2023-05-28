# PokerChip Detection YoloV5

 ### The Problem:
 The original idea is to count or track the number of chips assigned to a player, Reasons for a system would lead to tracking fraud chips, data collection and analysis of player behaviour and automatic chip counting systems using a mix of computer vision, count of chips on the table and per person.
 <br/>

 ### Data Collection and Preparation: 
 Images are collected from youtube video and image urls.  <br />
 From the image file the data is anottated using labelImg repo. <br />
 The annotations are stored into yolo format .txt file for each corresponding image, then organised into a dataset folder containing train and valid files with seperate annotation and image files. <br />   

 ### Framework:
Tensorflow <br /> 
YoloV5 <br />

 ### Training: 
 training is performed at 130 epochs. <br />
 training 130 epochs with 300 images took about an hour<br />
 30 epochs test runs <br />
 No specific reason for 130 epochs besides making sure there was enough training  <br />

## Evaluation:
Graphs and training metrics are provided, in this case most of the evaluation was observed by the live performance of video testing.
![http://url/to/img.png](https://github.com/Jpaku93/PokerChipDetection-YoloV5/blob/main/sample_img.png)


## Overview:
The object detection model (YoloV5) performs extremely well. After a 4 or 5 iterations of training the model detects most cases of poker chips <br /><br />

The first model identified more false positives than positives at a threshold of 70 with 30 epochs training, after succesfully increasing the epochs and threshold the model struggled to identify a majority of poker chips so another iteration of training data was annotated. <br /><br />

Within the next few trials were attempts to identify multiple labels for poker chips such as stack of chips, bundle of chips and single chip but too many false positives appeared. The final model was trained on overall pokerchips, single bundle, stacks and piles. <br /><br />

Overall the final model is not the optimal output but performs well to identify the majority of the chips from certain angles and different colors. <br />

## Dependencies: 
    pip install pytube
    pip install requests
    pip install opencv-python
    pip install lxml
    pip install PyQt5
    pip install ultralytics



## Installation Instructions:
- git clone https://github.com/Jpaku93/PokerChipDetection-YoloV5.git
- cd PokerChipDetection-YoloV5
- python -m venv env
- ./env/Scripts/activate
- python -m pip install --upgrade pip
- install dependencies
- copy image or video url to url_image.txt or url_video.txt
- git clone https://github.com/heartexlabs/labelImg.git
- cd labelImg
- pyrcc5 -o libs/resources.py resources.qrc
- python labelImg.py
- click open dir # open image folder (data/images)
- click the box containing (createML, Pascal<Voc>, yolo) to save as yolo format 
- annotate images and label data
- python prepare_data.py
- git clone https://github.com/ultralytics/yolov5  # clone
- cd yolov5
- pip install -r requirements.txt
- move dataset.yaml to yolov5
- python train.py --img 415 --batch 16 --epochs 30 --data dataset.yaml --weights yolov5s.pt --cache
- At the end of the training, two files should be saved in yolov5/runs/train/exp/weights: last.pt and best.pt. We’ll use best.pt.
- python -c "import matplotlib.pyplot as plt; import matplotlib.image as mpimg; image = mpimg.imread('runs/train/exp2/val_batch0_pred.jpg'); plt.imshow(image); plt.axis('off'); plt.show()" # ensure the exp[number] and [image] path is correct  
- python detect.py --source runs/train/exp2/a.jpg --weights best.pt
- python -c "import matplotlib.pyplot as plt; import matplotlib.image as mpimg; image = mpimg.imread('runs/detect/exp4/a.jpg'); plt.imshow(image); plt.axis('off'); plt.show()"
 
## References:
 repo ref: 
 - https://github.com/heartexlabs/labelImg.git
 - https://github.com/ultralytics/yolov5 
 - https://github.com/AarohiSingla/yolov5/blob/main/yolov5ontrafficsigndetection.ipynb <br />
 Research ref: https://patents.google.com/patent/US5781647A/en

## Continuous Improvement: 
 For now this work is baseline yolo object detection, <br />
 chip counting is complex for computer vision due to occlusion. <br />
 The research reference confirms my idea of data integrated references for weighted summary of players total chips. <br />
 sub classes might do better at robust precision detection such as considering all the chips on the table OR, <br />
 computer vision is better suited for sub task such as game monitoring and fraud chip detection.
 
