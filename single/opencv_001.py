import cv2
import numpy as np
case_path = '/usr/local/lib/python3.7/site-packages/\
            cv2/data/haarcascade_frontalcatface.xml'
faceCascade = cv2.CascadeClassifier(case_path)
imagename = cv2.imread("/Users/gangch/Downloads/CV0002721.jpg")
gray = cv2.cvtColor(imagename,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(faceCascade,gray,scaleFactor=1.1,minNeighbors=3,
                                     flags=cv2.CASCADE_FIND_BIGGEST_OBJECT,minSize=(5,5))

cv2.rectangle(imagename,(10,imagename.shape[0]-20),
              (110,imagename.shape[0]),(0,0,0),-1)
cv2.putText(imagename,"Find"+str(len(face))+ "face!",
            (10,imagename.shape[0]-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
for (x,y,w,h) in faces:
    cv2.rectangle(imagename,(x,y),(x+w,y+h),(128,255,0),2)
cv2.namedWindow("facedetect")
cv2.imshow("facedetect",imagename)
cv2.waitKey(0)
cv2.destroyWindow("facedectect")