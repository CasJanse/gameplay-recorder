from InputListener import InputListener
from ScreenRecorder import ScreenRecorder
import win32gui
import time
import cv2
import keyboard

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

    # Keep recording until the loop is broken by pressing q
    while True:
        # Break the loop when done
        if keyboard.is_pressed('q'):
            write_video_file(total_frames)
            break

        # Take a screenshot
        time.sleep(1 / fps)
        frames.append(screen_recorder.take_screenshot())

        # Get the input and save the frame every half second
        if len(frames) >= fps / 2:
            player_input = input_listener.get_keys_pressed_down()
            input_listener.clear_key_list()

            total_frames.append(frames)
            total_input.append(player_input)

            frames = []
            player_input = []


# Takes all the separate frames and writes them to a video file
def write_video_file(total_frames):
    out = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (window[2] - window[0], window[3] - window[1]))

    # Loop through the list to get to each frame and add is to the VideoWriter
    for i in range(len(total_frames)):
        for j in range(len(total_frames[i])):
            for k in range(len(total_frames[i][j])):
                # writing to a image array
                print(total_frames[i][j][k])
                print("---------------")
                out.write(total_frames[i][j][k])
    out.release()

# Wait a few seconds in order to focus on the correct window
time.sleep(1)
window = get_window_position()
print(window)


# Set the input listener and screen recorder
input_listener = InputListener()
screen_recorder = ScreenRecorder(window)

start_recording()



