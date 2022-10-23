import cv2
import os
import time
import mediapipe as mp
from cvzone.PoseModule import PoseDetector

detector = PoseDetector()
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


def show_fps(img, p_time):
    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time
    cv2.putText(
        img=img,
        text=str(int(fps)),
        org=(30, 50),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        fontScale=3,
        color=(255, 0, 255),
        thickness=4
    )
    return img, p_time


def fn(img, percentage=60):
    scale_percent = percentage  # 60  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized
