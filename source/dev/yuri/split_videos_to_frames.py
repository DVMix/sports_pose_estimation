import os
import numpy as np
import argparse
import cv2


# def main():
#     # parse all args
#     parser = argparse.ArgumentParser()
#     parser.add_argument('source',default='/home/yuri/Downloads/videos/', type=str, help='Path to source video')
#     parser.add_argument('dest_folder',default='/home/yuri/PycharmProjects/sports_pose_estimation/source/dev/yuri/frames/', type=str, help='Path to destination folder')
#     args = parser.parse_args()
#
#     # get file path for desired video and where to save frames locally
#     cap = cv2.VideoCapture(args.source)
#     path_to_save = os.path.abspath(args.dest_folder)
#
#     current_frame = 1
#
#     if (cap.isOpened() == False):
#         print('Cap is not open')
#
#     # cap opened successfully
#     while (cap.isOpened()):
#
#         # capture each frame
#         ret, frame = cap.read()
#         if (ret == True):
#
#             # Save frame as a jpg file
#             name = 'frame' + str(current_frame) + '.jpg'
#             print(f'Creating: {name}')
#             cv2.imwrite(os.path.join(path_to_save, name), frame)
#
#             # keep track of how many images you end up with
#             current_frame += 1
#
#         else:
#             break
#
#     # release capture
#     cap.release()
#     print('done')
#
#
# if __name__ == '__main__':
#     main()

import cv2


# Function to extract frames
def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        if count % 20 ==0:
            cv2.imwrite("frames/frame%d.jpg" % count, image)

        count += 1


# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture("/home/yuri/Downloads/run4.mp4")