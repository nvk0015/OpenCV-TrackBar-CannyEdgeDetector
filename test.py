import cv2
import numpy as np

def nothing(x):
    pass
cv2.namedWindow('Edge Tracker')
##creating the Trackbar
cv2.createTrackbar('lowerThreshold','Edge Tracker',0,255,nothing)
cv2.createTrackbar('upperThreshold','Edge Tracker',0,255,nothing)

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    lowerThreshold = cv2.getTrackbarPos('lowerThreshold','Edge Tracker')
    upperThreshold = cv2.getTrackbarPos('upperThreshold','Edge Tracker')
    img = cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)
    gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img,lowerThreshold,upperThreshold)
    image = np.concatenate((gray_scale,edges),axis=1)
    cv2.imshow('Live Stream', image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()