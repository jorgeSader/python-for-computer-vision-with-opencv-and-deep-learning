import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../../course/DATA/dog_backpack.jpg')

def draw_circle(event, x, y, flags, params):
  
  if event == cv.EVENT_RBUTTONDOWN:
      cv.circle(img, (x,y),150, (0,0,255), thickness=10)

cv.namedWindow(winname = 'backpack_dog')

cv.setMouseCallback('backpack_dog', draw_circle)

while True:
    cv.imshow('backpack_dog', img)
    
    if cv.waitKey(1) & 0xFF == 27:
        break
    
cv.destroyAllWindows()