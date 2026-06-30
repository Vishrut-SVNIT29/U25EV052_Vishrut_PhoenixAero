#Q17 Detect white landing pad with opencv

import cv2

#read image
img = cv2.imread("landing.jpg")

#convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#isolating white objects
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

#find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:

    #approximate contour shape
    approx = cv2.approxPolyDP(contour,0.02 * cv2.arcLength(contour, True),True)

    if len(approx) == 4:

        cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)

        print("Landing")

#save output image
cv2.imwrite("sahi.jpg", img)

#display result
cv2.imshow("Landing Pad Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()