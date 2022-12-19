# ウィンドウの調整

import cv2

img = cv2.imread("src/Lena.jpg")
cv2.namedWindow("window", cv2.WINDOW_AUTOSIZE)  # ウィンドウサイズ固定
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("src/Lena.jpg")
cv2.namedWindow("window", cv2.WINDOW_NORMAL)  # ウィンドウサイズ可変
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("src/Lena.jpg")
cv2.resizeWindow("window", 600, 400)  # ウィンドウサイズ指定
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
