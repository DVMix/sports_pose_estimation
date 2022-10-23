import cv2
import os


def main(path):
    if os.path.exists(path):
        cap = cv2.VideoCapture(path)

        counter = 0
        while True:
            success, img = cap.read()
            if success:
                cv2.imwrite(f'./test/{counter}.jpg', img)
                counter += 1


if __name__ == '__main__':
    path = 'D:\\programming\\PycharmProjects\\RTA\\video\\test.mp4'
    main(path=path)
