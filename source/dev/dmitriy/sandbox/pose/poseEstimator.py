import os
import cv2
import time

import mediapipe as mp
from botCore import original_video_folder, processed_video_folder

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


def process_single_frame(img):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    return results


def get_statistics(video_file, image_size, fps, landmarks=True, statistics=False, show_fps=False):
    original_path = os.path.join(original_video_folder, video_file)
    cap = cv2.VideoCapture(original_path)
    target_path = os.path.join(processed_video_folder, video_file)
    out = cv2.VideoWriter(target_path, cv2.VideoWriter_fourcc(*'MP4V'), fps, image_size)

    while True:
        success, img = cap.read()
        if success:
            results = process_single_frame(img)
            if results.pose_landmarks is not None and landmarks == True:
                mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

            out.write(img)
            cv2.imshow('Image', img)
            cv2.waitKey(10)
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# if show_fps:
#     c_time = time.time()
#     fps = 1 / (c_time - p_time)
#     p_time = c_time
#     cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255))
