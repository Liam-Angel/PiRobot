
from PIL import Image
#import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;
import serial
import time

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

  # Countours (needs canny)
  contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  print("Number of Contours Found = " + str(len(contours)))
  #image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
  cv2.drawContours(image, contours, -1, (255,255,255),2) 

  cv2.imshow('image', image)

  
  ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
  ser.reset_input_buffer()
    
  
  ser.write(b"move\n")
  time.sleep(1)
        
        # If there is a serial message waiting
  if ser.in_waiting > 0:
            
            # Decode and write it out to console
      line = ser.readline().decode('utf-8').rstrip()
      print(line)

 






  key = cv2.waitKey(1)
  if key == 27: # exit on ESC
    break


cam.release()
cv2.destroyAllWindows()
