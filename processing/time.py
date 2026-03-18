
from PIL import Image
#import pytesseract
import cv2 as cv
import os, sys, inspect #For dynamic filepaths
import numpy as np;

#Find the execution path and join it with the direct reference
cam = cv.VideoCapture(0)

while True: 
  check, frame = cam.read()
  image = cv.resize(frame,(320,240))

  image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

  # Threshold         120 is threshold, 255 is what we assign if it is below this
  _, image = cv.threshold(image, 150, 255, cv.THRESH_BINARY)

  # Canny
  image = cv.Canny(image, 30,200)

  contours, hierarchy = cv.findContours(image,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
  cv.drawContours(image, contours, -1, (255,255,255),2) 

  if len(contours) > 0:  
   cnt = contours[0]
   M = cv.moments(cnt)

   perimeter = cv.arcLength(cnt, True)
  
   print( perimeter )

   for perimiter in perimiter:



   imageC = cv.cvtColor(image, cv.COLOR_BGR2RGB)

   x,y,w,h = cv.boundingRect(cnt)
   cv.rectangle(imageC,(x,y),(x+w,y+h), (0, 255, 0),2)

  
  
  cv.imshow('imageC', imageC)

  key = cv.waitKey(1)
  if key == 27: # exit on ESC
    break


cam.release()
cv.destroyAllWindows()
