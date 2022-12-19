# γ変換
# γ変換の式を用いることで画像の明るさを調整することができる
# γが1より大きければ明るく、小さければ暗くなる

import cv2
import numpy as np

gamma = 1.5
img = cv2.imread("src/Berry.jpg")
gamma_cvt = np.zeros((256, 1), dtype=np.uint8)
for i in range(256):
    gamma_cvt[i][0] = 255 * (float(i) / 255) ** (1.0 / gamma)

img_gamma = cv2.LUT(img, gamma_cvt)

cv2.imshow("img", img)
cv2.imshow("gamma", img_gamma)
cv2.waitKey(0)
cv2.destroyAllWindows()
