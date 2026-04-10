import numpy as np
import cv2

# call casecade classifieers
face_class = cv2.CascadeClassifier(r'face_default.xml')
eye_class = cv2.CascadeClassifier(r'eye.xml')
# check whether the file is available or not
if face_class.empty():
    print("not file founded")
    exit()
if eye_class.empty():
    print("not file founded")
    exit()
image = cv2.imread(r'samvedya_ai.png')

#check the image loded or not
'''if not image.isOpen():
    print("no image is found")
    exit()'''
# convert the image to gray scale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# detect the faces in the image
face = face_class.detectMultiScale(gray,1.3,5)
eye = eye_class.detectMultiScale(gray,1.3,5)

# draw rectangle around the faces
for (x,y,w,h) in face:
    cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,255),2)
    for (ex,ey,ew,eh) in eye:
        cv2.rectangle(image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
# show the output image
cv2.imshow("face detection",image)
cv2.waitKey()
cv2.destroyAllWindows()
