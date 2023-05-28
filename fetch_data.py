# read lines from txt file
# download images from url
from pytube import YouTube
import requests
import os
import cv2

# read lines from txt file
def read_lines_from_txt_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    try:
        # get content between ""
        lines = [line.split('"')[1] for line in lines]
    except:
        pass 
    return lines


def download_images(url_list):
    # make directory if not exist
    save_directory_images = 'data/images'
    if not os.path.exists(save_directory_images):
        os.makedirs(save_directory_images)

    # Download the images from the URL list    
    for i in url_list:
        try:
            # Send a GET request to the URL
            response = requests.get(i)
            
            # Extract the filename from the URL
            filename = os.path.join(save_directory_images, i.split("/")[-1])
            
            # Save the image to the specified directory
            with open(filename, "wb") as file:
                file.write(response.content)
        except:
            print(f"Exception {i}:")

def download_youtube_video(url_list):
    save_directory_videos = "data/videos"    
    # make directory if not exist
    if not os.path.exists(save_directory_videos):
        os.makedirs(save_directory_videos)
    
    save_directory_frames = f'data/images'
    if not os.path.exists(save_directory_frames):
        os.makedirs(save_directory_frames)

    # download youtube videos
    for i in url_list:
        try:
            # Set the desired resolution, e.g., "720p", "1080p", "480p", etc.
            desired_resolution = "480p"  
            # Download the YouTube video
            yt = YouTube(i)
            video = yt.streams.filter(res=desired_resolution).first()
            path = video.download(save_directory_videos)
        except:
            print(f"Exception {i}:")

def extract_frames_from_videos():
    videos = os.listdir('data/videos')
    for i, video in enumerate(videos):
        # Extract frames every 10 seconds
        vidcap = cv2.VideoCapture(f"data/videos/{video}")
        success,image = vidcap.read()
        count = 0
        while success:
            if count % 2000 == 0:
                cv2.imwrite(f"data/images/{i}frame{count}.jpg", image)
            success,image = vidcap.read()
            count += 1
        # When everything done, release the capture
        vidcap.release()
        print (f"Extracted {count} frames from {video}!")

if __name__=="__main__":
    # download images from url and save in dataset file
    download_youtube_video( read_lines_from_txt_file('url_video.txt') )
    print("Videos downloaded successfully!")

    # download images from url and save in dataset file
    download_images(read_lines_from_txt_file('url_image.txt'))
    print("Images downloaded successfully!")

    # extract frames from videos 
    extract_frames_from_videos()