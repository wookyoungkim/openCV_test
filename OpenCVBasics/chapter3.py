import cv2

# reading image
img = cv2.imread("resources/chiiro.jpg")
print(img.shape)

#Resizing Image -> width, height
imgResize = cv2.resize(img, (300, 300))

#Crop Image -> height, width
imgCropped = img[0:200, 200:500]

cv2.imshow("output_img", img)
cv2.imshow("resize Image", imgResize)
cv2.imshow("crop Image", imgCropped)
cv2.waitKey(0)