import cv2

img = cv2.imread("PRO-104-OpenCV-Image-Assets-main/butterfly.jpg")
greyImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.putText(greyImg, "Butterfly", (20, 200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,0,255))
cv2.imshow("Butterfly", greyImg)

#print(greyImg)

cv2.waitKey(0)