# 動画の表示・出力

import cv2
import sys

cap = cv2.VideoCapture("movie/Cosmos.mp4")
if cap.isOpened() == False:
    sys.exit()
ret, frame = cap.read()  # cap.read():動画を1フレームずつ読み込む, ret:正しく読み込めたかどうか, frame:画像データ
h, w = frame.shape[:2]
fourcc = cv2.VideoWriter_fourcc(*"XVID")
dst = cv2.VideoWriter("output/test.avi", fourcc, 30.0, (w, h))

while True:  # 無限ループ
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow("img", frame)
    dst.write(frame)
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
cap.release()
