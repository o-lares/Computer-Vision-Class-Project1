# Computer-Vision-Class-Project
## Project for ELEE6280
## Image Tracking using OpenCV in Python

This project aims to demonstrate how to perform image tracking using python. I utilized OpenCV, a computer vision library, to implement the tracking. Image tracking is the process of analyzing successive frames of an image or video sequence to determine the movement of objects within the scene.

###Features Used
I utilized the ORB (Oriented FAST and Rotated BRIEF) feature detector to extract features from the images. These features are basically key points or landmarks that are distinctive and can be easily tracked from one image to another. I settled on ORB over SIFT, mainly to see how this algorithm worked but also because from what I read, it is a much faster algorithm, and it seemed simple to implement. I would like to use SIFT on future homeworks to see how it works in relation to ORB.

###Matching Algorithm
I used the Brute-Force Matcher, a common feature matching algorithm, to match the features between the images. The algorithm computes the Euclidean distance between the feature descriptors in two images, and returns the best match. I mainly saw it being used in the codes I referenced and figured the implementation was simple enough that I could use it fast to first get familiar with this computer vision task.

###Tracking Accuracy
To measure the accuracy of the tracking, I first calculated the number of correctly matched features between consecutive frames, and divided it by the total number of features detected in the previous frame. This gave me a percentage of how many features were accurately tracked.

###Results
The tracking results are displayed as a video which shows the cross frame tracking effect. A tracking accuracy of around 60% was obtained on our dataset of 200 images. I previously tried using the knn match method using k=2 but got worse accuracy results. Additionally, converting the images to black and white also helped to increase accuracy. In the first implementation the accuracy was around 40%. I think the BW images helped create more distinctive keypoints for the algorithm to detect.

###Conclusion
In this project, it was demonstrated how to perform image tracking using OpenCV in Python. I utilized the ORB feature detector and Brute-Force Matcher to track features in the sequence of 200 images provided and outlined the accuracy as well as some other methods tested to land on the final results.
