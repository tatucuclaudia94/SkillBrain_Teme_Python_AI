import cv2
import numpy as np

# incarcare imagine

img = cv2.imread("imagine.jpg")

# detectare obiecte albastre

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100,150,0])
upper_blue = np.array([140,255,255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Obiecte albastre", result)

# detectare contururi

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray,127,255,0)

contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    area = cv2.contourArea(cnt)

    if area > 500:

        x,y,w,h = cv2.boundingRect(cnt)

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Contururi", img)

# threshold adaptiv

adaptive = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

cv2.imshow("Adaptive Threshold", adaptive)

# canny + contururi

edges = cv2.Canny(gray,100,200)

contours,_ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    cv2.drawContours(img,[cnt],-1,(255,0,0),2)

cv2.imshow("Canny Contours", img)

# inchidere program

cv2.waitKey(0)

cv2.destroyAllWindows()

