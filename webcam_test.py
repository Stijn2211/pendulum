import numpy as np
import cv2 as cv
import matplotlib
import serial 
import time 

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1) 
def write_read(x): 
    arduino.write(bytes(x, 'utf-8')) 
    time.sleep(0.005) 
    #data = arduino.readline() 
    #return data 

vid = cv.VideoCapture(0)

while(True): 
      
    # Capture video
    ret, frame = vid.read()
    # Convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Binary threshold
    ret, th1 = cv.threshold(gray, 200, 255, 0)
    # Find contours
    contours, hierarchy = cv.findContours(th1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # Find largest contour (by area)
    if contours:
        c = max(contours, key = cv.contourArea)
        x,y,w,h = cv.boundingRect(c)
        # Draw green rectangle around largest contour
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    # Find center
        M = cv.moments(c)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv.circle(frame, (cx, cy), 7, (0, 0, 255), -1)
            print(cx)
            write_read(str(cx))
        # Draw all contours
        cv.drawContours(frame, contours, -1, (0,122,122), 1)
    # Display the resulting frame 
    cv.imshow('frame', frame) 
    # Exit loop by pressing q
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 