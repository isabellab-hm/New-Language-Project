#SOURCES:
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# https://github.com/arunponnusamy/cvlib
# https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/

import cv2
import cvlib as cv

cap = cv2.VideoCapture(0) # This will open a connection to the webcam of my phone

if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces, confidences = cv.detect_face(frame)

    for face in faces: # Looping through each face's box
        startX, startY, endX, endY = face
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0,255,0),2)# This should draw a box around each identified face
        
    count_text = f"People in room: {len(faces)}"

    # This will display the number of ppl identified on screen
    cv2.putText(frame, count_text,
                (12, 65),
                cv2.FONT_HERSHEY_TRIPLEX,
                2,
                (245, 66, 70),
                3)
    
    cv2.imshow("result", frame)
   
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows