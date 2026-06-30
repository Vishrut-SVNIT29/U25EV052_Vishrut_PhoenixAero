#Q19 Drone Color Marker Detection

import cv2
import numpy as np

#open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Unable to access webcam.")
    exit()

while True:

    #reading frame
    ret, frame = cap.read()

    if not ret:
        break

    #converting image from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower red color range
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    #upper red color range
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    #creating masks
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    #combining
    mask = mask1 + mask2

    # Find contours
    contours, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #draw rectangle around detected red objects
    for contour in contours:

        #condition to filter out small contours
        if cv2.contourArea(contour) > 500:

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(frame,(x, y),(x + w, y + h),(0, 255, 0),2)

            cv2.putText(frame,"Red Marker",(x, y - 10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0, 255, 0),2)

    cv2.imshow("Red Marker Detection", frame)

    #press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()