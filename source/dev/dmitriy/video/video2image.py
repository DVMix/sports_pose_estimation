import cv2
import os
from pathlib import Path


def convert_video_to_image_raw(path: str, save_folder: str = None) -> None:
    if os.path.exists(path):
        cap = cv2.VideoCapture(path)

        frame_number = 0
        while True:
            success, img = cap.read()
            if success:
                cv2.imwrite(f'./{Path(path).stem}/{frame_number}.jpg', img)
                frame_number += 1


def main():
    path = 'original/test.mp4'
    convert_video_to_image_raw(path)


if __name__ == '__main__':
    main()
