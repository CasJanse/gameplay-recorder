from InputListener import InputListener
# from ScreenRecorder import ScreenRecorder
import win32gui
import cv2
import numpy as np
import pyautogui
import time
import copy
import csv

fps = 15

# Get the position of the window currently in focus
# @return window_rect: A tuple containing the x, y, width and height of the window
def get_window_position():
    window = win32gui.GetForegroundWindow()
    window_rect = win32gui.GetWindowRect(window)
    win32gui.SetForegroundWindow(window)
    return window_rect


# Starts recording the screen and keyboard inputs
def start_recording():
    start_time = time.time()
    frame_amount = 0
    frame_timestamp = time.time()

    input_list = []

    # Keep recording until the loop is broken
    while True:
        # Record a frame whenever enough time has passed since the previous frame
        if time.time() - frame_timestamp >= 1 / fps or frame_amount == 0:
            # Take the screenshot
            frame_timestamp = time.time()
            img = pyautogui.screenshot(region=(window[0], window[1], window[2] - window[0], window[3] - window[1]))
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Show the recording in a separate screen if needed (disabled for performance optimisation)
            # cv2.imshow("Screen", frame)

            frame_amount += 1
            out.write(frame)

            # Get the keys that are currently held down
            input = copy.copy(input_listener.get_keys_pressed_down())
            input_list.append(input)

            # Stop the recording after x seconds
            # TODO: Change break to a key instead of timer
            if time.time() - start_time > 10:
                out.release()
                save_inputs_to_file(input_list)
                break


def save_inputs_to_file(input_list):
    with open("../input/inputs.csv", "w+") as result_file:
        writer = csv.writer(result_file, dialect="excel")
        writer.writerows(input_list)


# Wait a few seconds in order to focus on the correct window
time.sleep(1)
window = get_window_position()
print(window)

# Setup for the video capturing and writing
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("../video/output.avi", fourcc, fps, (window[2] - window[0], window[3] - window[1]))

# Set the input listener
input_listener = InputListener()

start_recording()



