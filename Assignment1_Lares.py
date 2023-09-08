#!/usr/bin/env python
# coding: utf-8

# Assignment 1 for ELEE6280 - by Oscar Lares

# Some parts of code adapted from these 2 sources: 
# https://medium.com/data-breach/introduction-to-orb-oriented-fast-and-rotated-brief-4220e8ec40cf
# https://github.com/tshanmukh/Facial-KeyPoint-Detection/blob/master/ORB.ipynb

# Submitted 2/26/2023

#import cv2 and os module needed
import os
import cv2

#specifying folder path and extension for where images are stored
folder_path = 'add your path here'
extension = '.png'

#load images into an array, use os.listdir to access folder path and read images in loop
images = []
for filename in sorted(os.listdir(folder_path)):
    if filename.endswith(extension):
        image = cv2.imread(os.path.join(folder_path, filename))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        images.append(gray)

#create ORB feature detector and find ORB keypoints and descriptors for first image
orb = cv2.ORB_create()
kp, desc = orb.detectAndCompute(images[0], None)

#create a Brute Force matcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

#initialize total keypoint and matched keypoints to help keep track of accuracy
total_kp = 0
matched_kp = 0

#create videowriter object to save tracking results to video format
fourcc = cv2.VideoWriter_fourcc(*'H264')
videowriter = cv2.VideoWriter('video_lares.mp4', fourcc, 10, images[0].shape[::-1])

#create loop for remaining images after getting kp and desc for first one in order to track the features
for i in range(1, len(images)):
    
    #find ORB keypoints and descriptors for image 'i'
    kp2, desc2 = orb.detectAndCompute(images[i], None)
    
    #perform the matching between the ORB descriptors of the current image and the previous image
    matches = bf.match(desc, desc2)

    #the matches with shorter distance are the ones we want
    matches = sorted(matches, key = lambda x : x.distance)
            
    #draw match and keypoints for video write      
    img_match = cv2.drawMatches(images[i-1], kp, images[i], kp2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imshow('Matches', img_match)
    cv2.waitKey(2)
    
    #update kp and desc for the next iteration in the loop
    kp, desc = kp2, desc2
    
    #update the count on matched and total keypoints for accuracy calculations later on
    total_kp += len(kp2)
    matched_kp += len(matches)
    
    #write tracking results to the output video
    videowriter.write(img_match)
    
#end the video writer object and destroy all windows
videowriter.release()
cv2.destroyAllWindows()

# Calculate and display the matching accuracy
matching_accuracy = matched_kp / total_kp * 100
print(f'Total keypoints: {total_kp}')
print(f'Matched keypoints: {matched_kp}')
print(f'Matching accuracy: {matching_accuracy:.2f}%')
