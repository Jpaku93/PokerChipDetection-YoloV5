# split train and test data 
# TODO: 
    #  read image folder
    #  split xml and corresponding image to label and image folder
    #  split train and test data 

import os
import shutil
import random
import xml.etree.ElementTree as ET

@function
def sort_training_files():
    # split xml and corresponding image to label and image folder
    # if image doesnt exist make new folder
    if not os.path.exists("yolov5/data/images"):
        os.makedirs("yolov5/data/images")
    
    if not os.path.exists("yolov5/data/labels"):
        os.makedirs("yolov5/data/labels")
    # read images folder
    images = os.listdir("images")
    # read xml folder
    xmls = os.listdir("xmls")
    # loop through xmls
    len(xmls)

    



