import os
from random import choice
import shutil

### Split Anottated images ###
path = "data/images"
#setup ratio (val ratio = rest of the files in origin dir after splitting into train and test)
train_ratio = 0.8
val_ratio = 0.2

# get list of txt files in path
txt_files = [f for f in os.listdir(path) if f.endswith('.txt')]
# make list of jpg files from txt files without .txt
jpg_files = [f[:-4] for f in txt_files]
# remove any file name that is classes.txt
jpg_files = [f for f in jpg_files if f != 'classes']

# dataset file
train_x = 'dataset/images/train'
val_x = 'dataset/images/val'
train_y = 'dataset/labels/train'
val_y = 'dataset/labels/val'
# if dataset file does not exist, create it
if not os.path.exists(train_x):
    os.makedirs(train_x)
if not os.path.exists(val_x):
    os.makedirs(val_x)
if not os.path.exists(train_y):
    os.makedirs(train_y)
if not os.path.exists(val_y):
    os.makedirs(val_y)


#total count of annotatated images
count = len(jpg_files)
#counting range for cycles
countForTrain = int(len(jpg_files)*train_ratio)
countForVal = int(len(jpg_files)*val_ratio)


# pick random file from list of files
for i in range(countForTrain):
    file = choice(jpg_files)
    # copy file from origin to train
    shutil.copy(f'{path}/{file}.jpg', f'{train_x}/{file}.jpg')
    shutil.copy(f'{path}/{file}.txt', f'{train_y}/{file}.txt')
    # remove file from list
    jpg_files.remove(file)

for i in range(len(jpg_files)):
    # copy remaining files to val
    shutil.copy(f'{path}/{jpg_files[i]}.jpg', f'{val_x}/{jpg_files[i]}.jpg')
    shutil.copy(f'{path}/{jpg_files[i]}.txt', f'{val_y}/{jpg_files[i]}.txt')

### Create yaml file ###
# open classes.txt and read lines to list 
with open('data/images/classes.txt', 'r') as f:
    classes = f.readlines()
# remove \n from list
classes = [f.strip() for f in classes]


# create yaml file
with open('dataset.yaml', 'w') as f:
    f.write(f'train: ../{train_x}\n')
    f.write(f'val: ../{val_x}\n')
    f.write(f'nc: {len(classes)}\n')
    f.write(f'names: {classes}')
