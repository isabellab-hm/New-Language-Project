#SOURCES:
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# https://github.com/arunponnusamy/cvlib
# https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/

import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T","Y", "U","I","O","P"],
       ["A","S","D","F","G","H","J","K","L",";"],
       ["Z","X","C","V","B","N","M",",",".","/"]]


class Button():
     def __init__(self, pos,text, size=[85,85]):
          self.pos = pos
          self.size = size
          self.text = text
          x,y = self.pos
          w,h =self.size
          cv2.rectangle(img, self.pos, (x+w, y+h),(255,0,255),cv2.FILLED)
          cv2.putText(img,self.text,(x+20, y+65),cv2.FONT_HERSHEY_PLAIN,
                4, (255,255,255),4)


buttonList = []

while True:
    success, img = cap.read()

    if not success:
         print("Error: Cannot Open Camera")
         continue
    
    hands, img = detector.findHands(img)

    for x, key in enumerate(keys[0]):
     buttonList.append(Button([100*x+50,100], key))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
         break


# import cv2
# import cvlib as cv



# cap = cv2.VideoCapture(0) # This will open a connection to the webcam of my phone

# if not cap.isOpened():
#     print("Error: Cannot open camera")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     faces, confidences = cv.detect_face(frame)

#     for face in faces: # Looping through each face's box
#         startX, startY, endX, endY = face
#         cv2.rectangle(frame, (startX, startY), (endX, endY), (0,255,0),2)# This should draw a box around each identified face
        
#     count_text = f"People in room: {len(faces)}"

#     # This will display the number of ppl identified on screen
#     cv2.putText(frame, count_text,
#                 (12, 65),
#                 cv2.FONT_HERSHEY_TRIPLEX,
#                 2,
#                 (245, 66, 70),
#                 3)
    
#     cv2.imshow("result", frame)
   
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows