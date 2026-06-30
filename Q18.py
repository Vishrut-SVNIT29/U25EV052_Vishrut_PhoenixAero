#Q18 Drone Video Feed Edge Detection

import cv2

#opening webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Unable to access webcam.")
    exit()

while True:

    #capturing one frame
    ret, frame = cap.read()

    #if frame not captured
    if not ret:
        print("Failed to capture frame.")
        break

    #converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    #display original video
    cv2.imshow("Original Video", frame)

    #display edge detected video
    cv2.imshow("Edge Detection", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()