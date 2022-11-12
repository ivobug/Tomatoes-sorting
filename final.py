# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 01:57:41 2022

@author: Ivan
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


#Defining RGB min-max color values choosen by experimenting
min_blue=0  
min_green=0
min_red=0
max_blue=88
max_green=255 
max_red=255

video = cv2.VideoCapture('tomatoes.mp4')

while True:
    ret, frame = video.read()
    if not ret:
        break
    
    # converting image into HSV color space 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    #getting the mask image from the HSV image using threshold values
    mask = cv2.inRange(hsv_frame, (min_blue, min_green, min_red), (max_blue, max_green, max_red))
    #extracting the contours of the object
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #sorting the contour based of area
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    if contours:
        #if any contours are found we take the biggest contour and get bounding box
        (x_min, y_min, box_width, box_height) = cv2.boundingRect(contours[0])
        #drawing a rectangle around the object with 15 as margin
        cv2.rectangle(frame, (x_min - 15, y_min -15),
                      (x_min + box_width + 15, y_min + box_height + 15),
                      (0,255,0), 4)
        
    #showing each frame of the video 
    cv2.imshow('frame',frame)
    #slow down the video to see the results clearly
    time.sleep(0.01)
    key = cv2.waitKey(5)
    # waiting for q key to be pressed and then breaking
    if key == ord('q'):
        break
    

# When everything done, release the resources and destroy created windows
video.release()
cv2.destroyAllWindows() 