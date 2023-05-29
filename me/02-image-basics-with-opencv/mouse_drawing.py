import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Global Variables 
drawing = False
ix = -1
iy = -1

# Function To draw a rectangle
def draw_rectangle(event, x, y, flags, params):
  
    global ix, iy, drawing
  
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
    
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.rectangle(img, (ix, iy), (x,y), (0, 255, 0), thickness = 5 )
    
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img, (ix, iy), (x,y), (0, 255, 0), 5 )
      

# Create black image
img = np.zeros((512, 512,3))
cv.namedWindow(winname = 'my_drawing')
cv.setMouseCallback('my_drawing', draw_rectangle)

while True:
    cv.imshow('my_drawing', img)
    
    if cv.waitKey(1) & 0xFF == 27:
        break
    
cv.destroyAllWindows()