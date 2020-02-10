from InputListener import InputListener
from ScreenRecorder import ScreenRecorder
import win32gui
import time

def get_window_position():
    window = win32gui.GetForegroundWindow()
    window_rect = win32gui.GetWindowRect(window)
    win32gui.SetForegroundWindow(window)
    return window_rect


input_listener = InputListener()
screen_recorder = ScreenRecorder(0, 0, 500, 500)

time.sleep(3)
window = get_window_position()

# screen_recorder.record_screen()

print(get_window_position())



