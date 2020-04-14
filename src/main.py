from InputListener import InputListener
# from ScreenRecorder import ScreenRecorder
import win32gui
import cv2
import numpy as np
import pyautogui
import time
import copy
import csv
import os

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
    print("Start recording...")

    # Keep recording until the loop is broken
    while True:
        # Record a frame whenever enough time has passed since the previous frame
        if time.time() - frame_timestamp >= 1 / fps or frame_amount == 0:
            # Take the screenshot
            frame, frame_timestamp = take_screenshot()
            frame_amount += 1

            # width = int(frame.shape[1] * 5 / 100)
            # height = int(frame.shape[0] * 5 / 100)
            # dim = (width, height)

            # resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

            out.write(frame)

            # Show the recording in a separate screen if needed (disabled for performance optimisation)
            # cv2.imshow("Screen", frame)

            # Get the keys that are currently held down
            input_keys = copy.copy(input_listener.get_keys_pressed_down())

            # Stop the recording when the q key is pressed
            if "q" in input_keys:
                out.release()
                print("Video saved")
                save_inputs_to_file(input_list)
                break

            # Add the currently pressed keys to the list of inputs
            input_list.append(input_keys)


# Take a screenshot of the active window
# @return frame: The image taken of the active window (list)
# @return frame_timestamp: The time.time() that the current image was taken on
def take_screenshot():
    frame_timestamp = time.time()
    window = get_window_position()
    img = pyautogui.screenshot(region=(window[0] + left_offset, window[1] + top_offset, window[2] + right_offset - window[0] + left_offset, window[3] + bottom_offset - window[1] + top_offset))
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame, frame_timestamp


# Save the list of inputs to an external cvs file to be used later
def save_inputs_to_file(input_list):
    input_index = len([name for name in os.listdir('../../gameplay-data/input')])
    with open("../../gameplay-data/input/inputs_{}.csv".format(input_index), "w+") as result_file:
        writer = csv.writer(result_file, dialect="excel")
        writer.writerows(input_list)
    print("Input keys saved")


# Wait a few seconds in order to focus on the correct window
time.sleep(1)
window = get_window_position()
print(window)

top_offset = 80
bottom_offset = -200
left_offset = 25
right_offset = -90

# Setup for the video capturing and writing
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_index = len([name for name in os.listdir('../../gameplay-data/video')])
out = cv2.VideoWriter("../../gameplay-data/video/output_{}.avi".format(video_index), fourcc, fps, (int((window[2] + right_offset - window[0] + left_offset)), int((window[3] + bottom_offset - window[1] + top_offset))))

# Set the input listener
input_listener = InputListener()

start_recording()



