# マウスイベント

import cv2
import numpy as np


def print_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x, y)


img = np.zeros((512, 512), np.uint8)
cv2.namedWindow("img")
cv2.setMouseCallback("img", print_position)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
