# 色空間・グレースケール

import cv2

img = cv2.imread("src/grapes.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray2 = cv2.imread("src/grapes.jpg", 0)  # この方法でもグレーになる
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(img_gray.shape)  # 第3引数が消えている
print(img_hsv.shape)

cv2.imshow("img", img)
cv2.imshow("gray", img_gray)
cv2.imshow("gray2", img_gray2)
cv2.imshow("hsv", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
