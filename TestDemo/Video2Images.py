"""
    This file is to convert video to image frames for video compression
"""
import cv2
import os

from argparse import ArgumentParser

def main(video_filepath, outputfoldername):
    vidcap = cv2.VideoCapture(video_filepath)
    success,image = vidcap.read()
    count = 0
    output_prefix = "./"+outputfoldername+"/"

    if not os.path.exists(outputfoldername):
        os.mkdir(outputfoldername)
    while success:
        # Resize to desired sizes
        image = cv2.resize(image, (1280, 704))
        fullpath = output_prefix+"frame"+str(count)+".jpg"
        cv2.imwrite(fullpath, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        count += 1
    print("Extracted ",count,"frames")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--video', type=str, dest="video_filepath", default='./TestVideo/big_buck_bunny_720p_5mb.mp4', help="video file to be extracted")
    parser.add_argument('--outputfoldername', type=str, dest="outputfoldername", default='images', help="output folder for extracted images")

    args = parser.parse_args()
    main(**vars(args))