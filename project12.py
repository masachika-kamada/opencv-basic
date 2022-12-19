# 2値化

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("src/grapes.jpg", 0)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.THRESH_BINARYの場合は閾値を事前に設定する必要がある
threshold = 100
ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
print(ret)  # = threshold
cv2.imshow("img_th", img_th)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.THRESH_OTSUを使うと自動で閾値を調整してくれる
# ヒストグラムの分布が二山に分かれていることが条件
ret2, img_o = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
print(ret2)  # 0から更新されている
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()
cv2.imshow("otsu", img_o)
cv2.waitKey(0)
cv2.destroyAllWindows()

# adaptive_thresholdを用いると周囲と比較した明暗によって2値化がなされる
# 影の部分であっても相対的に判定するので白が含まれる
img_ada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1)
cv2.imshow("ada", img_ada)
cv2.waitKey(0)
cv2.destroyAllWindows()
