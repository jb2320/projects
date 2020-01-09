
import subprocess
import pip


#process = subprocess.Popen("cmd.exe", shell=False, universal_newlines=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE,stdout=subprocess.PIPE)
#process.communicate(
pip.main(['install','--upgrade', 'pip==9.0.3'])
pip.main(['install', 'numpy'])
pip.main(['install', 'opencv-python'])
import numpy as np
import cv2
import socket

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
ret,frame = cap.read() # return a single frame in variable `frame`

#cv2.imshow('img1',frame) #display the captured image
cv2.imwrite('c3.png',frame)
cv2.destroyAllWindows()

cap.release()