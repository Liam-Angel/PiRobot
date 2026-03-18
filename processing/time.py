
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
  rects = [cv.minAreaRect(c) for c in contours if cv.contourArea(c) > 100]

  linediff = 180
  pair = (None, None)
  

  if len(contours) > 2:  
   
   for cnt in contours:
    M = cv.moments(cnt)
    perimeter = cv.arcLength(cnt, True)
    epsilon = 10 * perimeter
    approx_contour = cv.approxPolyDP(cnt, epsilon, True)
    x,y,w,h = cv.boundingRect(cnt)
    rect = cv.minAreaRect(cnt)

    if perimeter >100 and h >  50:
      #print(perimeter)
      rows, cols = imageC.shape[:2]
      [vx, vy, x, y,] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0,0.01)
      lefty = int((-x*vy/vx)+y)
      righty = int(((cols-x)*vy/vx)+y)
      #cv.rectangle(imageC,(x,y),(x+w,y+h), (0, 255, 0),2)
      cv.line(imageC,(cols-1,righty),(0,lefty),(0,255,0),2)

   cv.imshow('imageC', imageC)




  
  

  key = cv.waitKey(1)
  if key == 27: # exit on ESC
    break


cam.release()
cv.destroyAllWindows()
