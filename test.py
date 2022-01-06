import cv2

def nothing(x):
    pass
cv2.namedWindow('Edge Detector')
##creating the Trackbar
cv2.createTrackbar('lowerThreshold','Edge Detector',0,255,nothing)
cv2.createTrackbar('upperThreshold','Edge Detector',0,255,nothing)

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    lowerThreshold = cv2.getTrackbarPos('lowerThreshold','Edge Detector')
    upperThreshold = cv2.getTrackbarPos('upperThreshold','Edge Detector')
    edges = cv2.Canny(img,lowerThreshold,upperThreshold)
    cv2.imshow('Live Video', img)
    cv2.imshow('Edge Detector',edges)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()