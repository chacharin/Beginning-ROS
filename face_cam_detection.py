#!/usr/bin/env python3
import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier("/home/home/Desktop/haarcascade_frontalface_default.xml")

# Read the input image
cap = cv2.VideoCapture(0)
fprint = False

while True:
    _, img = cap.read()

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.4, 3)


    if len(faces) >= 1 and fprint == False:
        print("Human detected",len(faces))
        fprint = True
        

    elif len(faces) < 1 and fprint == True:
        print("No Human detected",len(faces))
        fprint = False

    else:
        pass
    
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()