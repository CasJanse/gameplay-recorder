from InputListener import InputListener
# from ScreenRecorder import ScreenRecorder
import win32gui
import time
import cv2
import keyboard
import numpy as np
from PIL import ImageGrab

fps = 30


# Get the position of the window currently in focus
# @return window_rect: A tuple containing the x, y, width and height of the window
def get_window_position():
    window = win32gui.GetForegroundWindow()
    window_rect = win32gui.GetWindowRect(window)
    win32gui.SetForegroundWindow(window)
    return window_rect


# Starts recording the screen and keyboard inputs
def start_recording():
    frames = []
    player_input = []
    total_frames = []
    total_input = []

    # Keep recording until the loop is broken by pressing esc
    while True:
        img = ImageGrab.grab(bbox=window)
        img_np = np.array(img)

        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        out.write(frame)

        # Get the input and save the frame every half second
        if len(frames) >= fps / 2:
            player_input = input_listener.get_keys_pressed_down()
            input_listener.clear_key_list()

            frames = []
            player_input = []

        if keyboard.is_pressed('q'):
            break
    out.release()


# Wait a few seconds in order to focus on the correct window
time.sleep(3)
window = get_window_position()
print(window)


# Set the input listener and screen recorder
input_listener = InputListener()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("../video/output.avi", fourcc, 30, (window[2] - window[0], window[3] - window[1]))
# screen_recorder = ScreenRecorder(window)

start_recording()



