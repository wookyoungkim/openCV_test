import cv2
import numpy as np
import face_recognition

# loading image -> converting to rgb
imgElon = face_recognition.load_image_file('ImagesBasic/ElonMusk.png')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/ElonTest.png')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# finding faces
faceLoc = face_recognition.face_locations(imgElon)[0]
# encode face
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]),(faceLoc[1], faceLoc[2]), (255,0,255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]),(faceLocTest[1], faceLocTest[2]), (255,0,255), 2)

# detecting faces
results = face_recognition.compare_faces([encodeElon], encodeTest)
print(results)

# how similar? -> distance
faceDis = face_recognition.face_distance([encodeElon], encodeTest) # lower the distance, better the similarities
print(faceDis)

cv2.imshow("Elon Musk", imgElon)
cv2.imshow("Elon Test", imgTest)
cv2.waitKey(0)