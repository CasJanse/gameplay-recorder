import cv2
import numpy as np
import pyautogui
import time

start_time = time.time()
second = 1
frame_amount = 0
frame_timestamp = time.time()
fps = 20

while True:
    if time.time() - frame_timestamp >= 1 / fps or frame_amount == 0:
        frame_timestamp = time.time()
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # cv2.imshow("Screen", frame)
        frame_amount += 1

        if time.time() - start_time > 1:
            break

print(frame_amount)
# cv2.destroyAllWindows()