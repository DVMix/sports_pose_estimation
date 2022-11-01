# @TODO Получить скедет человека для 1 кадра
# @TODO реализовать конвертер результатов в челоекочитаемый формат
# @TODO реализовать алгоритм соотношения роста и скелета

import cv2
import mediapipe as mp
import yaml

with open("bodyDecoder.yaml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)

print('!')


class Body(object):
    def __init__(self):
        pass

    def head(self):
        raise Exception

    def arms(self, side):
        pass

    def legs(self, side):
        pass
