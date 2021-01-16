import cv2
import numpy as np

# 3. Get Contours
def getContuors(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        # 4. Draw Edges
        if area > 100:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)  # -1: draw all the contours
            # 5. Calculate the arc length
            peri = cv2.arcLength(cnt, True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(approx)
            # 6. Object coners
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # 7. Categorize the shapes
            if objCor == 3:
                ObjType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    ObjType = "Sqr"
                else: ObjType = "Rec"
            elif objCor > 4:
                ObjType = "Circle"
            else:
                ObjType = "None"

            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(imgContour, ObjType,
                        (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_SIMPLEX,  #pos for text
                        0.7, (0,0,0), 2)

path = 'resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

# 1. Convert into Grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)

# 2. Detect edges
imgCanny = cv2.Canny(imgBlur, 50, 50)

# 3. Get Contour
getContuors(imgCanny)
imgBlack = np.zeros_like(img)

cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Contour", imgContour)
cv2.waitKey(0)