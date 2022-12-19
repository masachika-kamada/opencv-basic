# 図形の描画・文字の記述

import cv2
import numpy as np

img = np.ones((500, 500, 3)) * 255

cv2.line(img, (0, 10), (200, 400), (255, 0, 0), 12)
cv2.rectangle(img, (100, 90), (400, 400), (0, 255, 0), 6)
cv2.circle(img, (280, 240), 100, (0, 0, 255), -1)
cv2.ellipse(img, (344, 260), (90, 40), 45, 0, 360, (255, 0, 0), 2)

pts = np.array([[45, 290], [178, 259], [350, 35], [100, 100]])
cv2.polylines(img, [pts], False, (100, 255, 0), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (200, 300), font, 1, (0, 255, 0), 3, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
