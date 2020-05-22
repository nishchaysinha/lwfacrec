import cv2
import sys

face_cascade=(cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml').load)
video_capture=cv2.VideoCapture(0)
test=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    #frame by frame analysis
    retval, frame=video_capture.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=test.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(35,35)
)

for(x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (50, 50, 200), 2)
cv2.imshow('Video', frame)

if cv2.waitKey(1) & 0xFF==ord('q'):
    sys.exit()
    
