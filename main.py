import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller
from playsound import playsound

cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T","Y", "U","I","O","P"],
       ["A","S","D","F","G","H","J","K","L",";"],
       ["Z","X","C","V","B","N","M",",",".","/"]]
finalText = ""

keyboard = Controller()

def drawALL(img, buttonList):
     for button in buttonList:
          x,y = button.pos
          w,h = button.size
          cv2.rectangle(img, button.pos, (x+w, y+h),(100, 150, 255),cv2.FILLED)
          
          fontScale = 4
          if button.text == "Del":
               fontScale = 2.5
          elif button.text == "Space":
               fontScale = 2.5
          else:
               fontScale = 4
          thickness = 4

          textSize = cv2.getTextSize(button.text, cv2.FONT_HERSHEY_PLAIN, fontScale, thickness)[0]
          textX = x + int((w - textSize[0]) / 2)
          textY = y + int((h + textSize[1]) / 2)
     
          cv2.putText(img, button.text, (textX, textY), cv2.FONT_HERSHEY_PLAIN,
                    fontScale, (255, 255, 255), thickness)
          
     return img

class Button():
     def __init__(self, pos,text, size=[85,85]):
       self.pos = pos
       self.size = size
       self.text = text


buttonList = []
for i in range(len(keys)): 
     for j, key in enumerate(keys[i]):
          buttonList.append(Button([100*j+50,100*i+50], key))

buttonList.append(Button([100*9+50, 100*3+50], "Del"))
buttonList.append(Button([100*0+50, 100*3+50], "Space", [500, 85]))

while True:
    success, img = cap.read()
    if not success:
         print("Error: Cannot Open Camera")
         continue
    
    hands, img = detector.findHands(img)

    lmList = []
    if hands:
       lmList = hands[0]["lmList"] 

    img = drawALL(img, buttonList)

    if lmList:
         for button in buttonList:
              x, y = button.pos
              w, h = button.size
              
              if x < lmList[8][0] <x+w and y<lmList[8][1]<y+h: #Index finger tip (8)
                       l, _, _ = detector.findDistance(lmList[8][:2],lmList[12][:2], img)
                       print(l)

                       if l < 30: 
                         cv2.rectangle(img, button.pos, (x + w, y + h), (0, 200, 0), cv2.FILLED) 
                       else:
                         cv2.rectangle(img, button.pos, (x+w, y+h), (130, 180, 255),cv2.FILLED)  

                       if button.text == "Del":
                         fontScale = 3
                       elif button.text == "Space":
                            fontScale = 3
                       else:
                         fontScale = 4.5
                       thickness = 4
                       textSize = cv2.getTextSize(button.text, cv2.FONT_HERSHEY_PLAIN, fontScale, thickness)[0]
                       textX = x + int((w - textSize[0]) / 2)
                       textY = y + int((h + textSize[1]) / 2)
                       cv2.putText(img, button.text, (textX, textY), cv2.FONT_HERSHEY_PLAIN,
                            fontScale, (255, 255, 255), thickness)

                       if l < 30: 
                         if button.text == "Del":
                                 if len(finalText) > 0:
                                      finalText = finalText[:-1]
                                      keyboard.press('\b')    
                         elif button.text == "Space":
                              finalText += " "
                              keyboard.press(' ')
                         else:
                                 keyboard.press(button.text)
                                 finalText += button.text

                         playsound('click.wav',block=False)
                         sleep(0.5)

                            
    cv2.rectangle(img, (50, 500), (1000, 600),(200, 230, 255),cv2.FILLED)
    cv2.putText(img, finalText,(60, 580),cv2.FONT_HERSHEY_PLAIN,
                          5, (255,255,255),5)     

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
         break