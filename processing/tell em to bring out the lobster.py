# You may run into issues installing pytesseract, this is because python wants you to install things into virtual environments
# For our usecase, venv aren't super useful as we are only making one project at a time, so use the flags below:
# sudo pip3 install pytesseract --break-system-packages
# https://nanonets.com/blog/ocr-with-tesseract/
from PIL import Image
#import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;

#Find the execution path and join it with the direct reference
cam = cv2.VideoCapture(0)

while True: 
  check, frame = cam.read()
  image = cv2.resize(frame,(320,240))



  # Greyscale
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Threshold         120 is threshold, 255 is what we assign if it is below this
  _, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)

  # Canny
  image = cv2.Canny(image, 30,200)

  ret,thresh = cv2.threshold(image,127,255,0) 

  # Countours (needs canny)
  contours1, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
  contours2, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

  ### Step #2 - Reshape to 2D matrices
  contours1 = contours1[0].reshape(-1,2)
  contours2 = contours2[0].reshape(-1,2)

  ### Step #3 - Draw the points as individual circles in the image
  img1 = image.copy()
  img2 = image.copy()

  for (x, y) in contours1:
      cv2.circle(img1, (x, y), 200, (255, 0, 0), 300)

  for (x, y) in contours2:
      cv2.circle(img2, (x, y), 200, (255, 0, 0), 300)

  cv2.imshow('image', image)

  key = cv2.waitKey(1)
  if key == 27: # exit on ESC
    break


cam.release()
cv2.destroyAllWindows()
