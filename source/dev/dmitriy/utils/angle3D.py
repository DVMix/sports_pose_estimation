import numpy as np
from collections import namedtuple
import math
import time


def get_angle(p0, p1, p2):
    radians = (p1.x * p2.x + p1.y * p2.y + p1.z * p2.z) / \
              (np.sqrt(np.power(p1.x, 2) + np.power(p1.y, 2) + np.power(p1.z, 2)) * \
               np.sqrt(np.power(p2.x, 2) + np.power(p2.y, 2) + np.power(p2.z, 2)))
    angle = round(np.rad2deg(np.arccos(radians)), 1)
    return radians, angle


def angle_2p_3d(a, b, c):

    v1 = np.array([ a[0] - b[0], a[1] - b[1], a[2] - b[2] ])
    v2 = np.array([ c[0] - b[0], c[1] - b[1], c[2] - b[2] ])

    v1mag = np.sqrt([ v1[0] * v1[0] + v1[1] * v1[1] + v1[2] * v1[2] ])
    v1norm = np.array([ v1[0] / v1mag, v1[1] / v1mag, v1[2] / v1mag ])

    v2mag = np.sqrt(v2[0] * v2[0] + v2[1] * v2[1] + v2[2] * v2[2])
    v2norm = np.array([ v2[0] / v2mag, v2[1] / v2mag, v2[2] / v2mag ])
    res = v1norm[0] * v2norm[0] + v1norm[1] * v2norm[1] + v1norm[2] * v2norm[2]
    angle_rad = np.arccos(res)

    return math.degrees(angle_rad)


def main():
    Point = namedtuple('Point', ['x', 'y', 'z'])
    p0 = Point(x=0, y=0, z=0)
    p1 = Point(x=1, y=1, z=1)
    p2 = Point(x=1, y=0, z=0)
    radians, angle = get_angle(p0, p1, p2)
    print(f'Success: {angle}({radians})')


if __name__ == '__main__':
    main()
