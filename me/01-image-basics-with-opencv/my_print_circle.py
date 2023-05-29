import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt

def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 100, (0,255,0), -1)
        
    elif event== cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), 100, (255, 0 ,0), thickness = 5)
        
cv.namedWindow(winname = 'my-drawing')

cv.setMouseCallback('my-drawing', draw_circle)

img = np.zeros(shape=(512,512,3))

while True:
    cv.imshow('my-drawing', img)
    
    if cv.waitKey(20) & 0xFF == 27:
        break
        
cv.destroyAllWindows()