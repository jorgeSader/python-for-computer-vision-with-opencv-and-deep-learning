
import cv2

img = cv2.imread('./course/DATA/00-puppy.jpg',cv2.IMREAD_GRAYSCALE)
# Show the image with OpenCV
while True:
    cv2.imshow('window_name',img)

    # Wait for something on keyboard to be pressed to close window.
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()