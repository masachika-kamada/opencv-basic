# 画像の表示・出力

import cv2
import os

img = cv2.imread("src/Berry.jpg")

print(img.shape)
print(img[0][0])

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

os.mkdir("./output")
cv2.imwrite("output/test.jpg", img)
