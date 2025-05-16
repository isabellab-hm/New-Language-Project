import cv2
import mediapipe as mp
print(mp.__version__)
import numpy as np
import time
import os

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

       # left_shoulder = (int(landmarks[mp.pose.PoseLandmark.LEFT_SHOULDER.value].x * frame.shape[1]), int(landmarks[mp.pose.PoseLandmark.LEFT_SHOULDER.value].x * frame.shape[1]))

# video = cv2.VideoCapture(0)

# while True:
#     status, frame = video.read()
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Change to gray scale format
#     gray = cv2.GaussianBlur(gray, (21,21), 0)
#     cv2.imshow("Gray Video", gray)
#     key = cv2.waitKey(1)