'''
GIT-"nishchaysinha.github.io"

to install type "git clone 'repo link'"

'''

import cv2
import sys

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    #frame-by-frame(24img/sec(default))
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv2.CASCADE_SCALE_IMAGE
    )

    #rectangle-overlay
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #display-with-rectangle-overlay
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#"CLEAR CACHE"
video_capture.release()
cv2.destroyAllWindows()
