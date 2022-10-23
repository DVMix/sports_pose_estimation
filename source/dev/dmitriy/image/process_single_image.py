import cv2
from cvzone.PoseModule import PoseDetector

# import os
# import time
# import mediapipe as mp
# mpDraw = mp.solutions.drawing_utils
# mpPose = mp.solutions.pose
# pose = mpPose.Pose()


detector = None


def init_detector():
    global detector
    detector = PoseDetector()


def process_single_frame(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    try:
        img_rgb = detector.findPose(img_rgb)
        results = detector.findPosition(img_rgb)
        return img_rgb, results
    except ModuleNotFoundError as e:
        raise e


if __name__ == "__main__":
    init_detector()
    image = cv2.imread('./test/0.jpg')
    img_rgb, results = process_single_frame(image)
    angle = detector.findAngle(img=img_rgb, p1=12, p2=14, p3=16)
    print('Success!')


