import cv2

# reading image
img = cv2.imread("resources/chiiro.jpg")
cv2.imshow("output_img", img)
cv2.waitKey(0)

#reading video
cap = cv2.VideoCapture("resources/chiiro_video.MP4")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#reading webcam
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
cam.set(10, 100)

while True:
    success, image = cam.read()
    cv2.imshow("Video", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break