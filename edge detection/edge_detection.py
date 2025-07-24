import cv2
import numpy as np

img = cv2.imread("illustration-of-multiple-objects-D001YY.jpg")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edge = cv2.Canny(blurred, 30, 100)
dilated = cv2.dilate(edge, None, iterations=2)
contours, hierar = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

object_count = 0
MIN_AREA_THRESHOLD = 100

draw_img = img.copy()

for c in contours:
    area = cv2.contourArea(c)
    if area > MIN_AREA_THRESHOLD:
        object_count += 1
        cv2.drawContours(draw_img, [c], -1, (0, 255, 0), 3)


cv2.resize(draw_img,(1400,10))
cv2.imshow("COUNTERS", draw_img)
cv2.imwrite("SAVE.JPG",draw_img)
print(len(contours))

cv2.waitKey(0)
cv2.destroyAllWindows()