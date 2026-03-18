
from PIL import Image
#import pytesseract
import cv2 as cv
import os, sys, inspect #For dynamic filepaths
import numpy as np;

#Find the execution path and join it with the direct reference
cam = cv.VideoCapture(0)

while True: 
  check, frame = cam.read()
  img = cv.resize(frame,(320,240))

  image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  image = cv.GaussianBlur(image, (11, 11), sigmaX=0)

  # Threshold         120 is threshold, 255 is what we assign if it is below this
  _, image = cv.threshold(image, 150, 255, cv.THRESH_BINARY)

  # Canny
  image = cv.Canny(image, 30,200)

  contours, hierarchy = cv.findContours(image,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
  cv.drawContours(image, contours, -1, (255,255,255),2) 
  imageC = cv.cvtColor(image, cv.COLOR_BGR2RGB)

  if len(contours) > 0:  
   for contour in contours:
    cnt = contour
    M = cv.moments(cnt)
    perimeter = cv.arcLength(cnt, True)
    epsilon = 100 * perimeter
    approx_contour = cv.approxPolyDP(cnt, epsilon, True)


    x,y,w,h = cv.boundingRect(cnt)
    cv.rectangle(imageC,(x,y),(x+w,y+h), (0, 255, 0),2)

   cv.imshow('imageC', imageC)




  
  

  key = cv.waitKey(1)
  if key == 27: # exit on ESC
    break


cam.release()
cv.destroyAllWindows()
