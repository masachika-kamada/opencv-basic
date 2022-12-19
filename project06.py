# ヒストグラム
# ヒストグラムを使うことで画像の中にRGBどれが多いかなど画素値の分布をみることができる

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("src/Lena.jpg")
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

color_list = ["blue", "green", "red"]
for index, item in enumerate(color_list):
    hist = cv2.calcHist([img], [index], None, [256], [0, 256])
    # calcHint([対象], [BGRのindex], マスクする画像があるか(default:None), [分解能], [範囲])
    plt.plot(hist, color=item)
    plt.show()

img_gray = cv2.imread("src/Lena.jpg", 0)
hist2 = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(hist2, color="gray")
plt.show()
