import cv2
import numpy as np

img=cv2.imread("eye.jpg")
#Converting to gray image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Blurring the image
blur_image=cv2.blur(gray,(3,3))

# Hough FOR EYE.jpg
detected_circles=cv2.HoughCircles(
    blur_image,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=20,
    param1=90,
    param2=35,
    minRadius=60,
    maxRadius=90)

# Hough for ee.jpg
# detected_circles=cv2.HoughCircles(
#     blur_image,
#     cv2.HOUGH_GRADIENT,
#     dp=1,
#     minDist=20,
#     param1=90,
#     param2=35,
#     minRadius=20,
#     maxRadius=50)

# FOR 998.jpg
# detected_circles=cv2.HoughCircles(
#     blur_image,
#     cv2.HOUGH_GRADIENT,
#     dp=1,
#     minDist=10,
#     param1=90,
#     param2=35,
#     minRadius=5,
#     maxRadius=40)

# Drawing circles on image
if detected_circles is not None:

    # Converting to int
    detected_circles=np.uint(np.around(detected_circles))

    for pt in detected_circles[0, : ]:
        a,b,r=pt[0],pt[1],pt[2]

        #Drawimg circles
        cv2.circle(img,(a,b),r,(0,255,0),2)

        cv2.imshow("Detected circle ",img)
        cv2.waitKey(0)