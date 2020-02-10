import mss
import mss.tools
import numpy as np
import cv2
import time
import random
from PIL import Image

# Takes a screenshot of the currently selected window
class ScreenRecorder:
    def __init__(self, window):
        self.x = window[0]
        self.y = window[1]
        self.width = window[2]
        self.height = window[3]

        self.monitor = {}
        self.image_size = {}

        self.key_index = 0
        self.resize_scale = 4

        self.set_coordinates(self.x, self.y, self.width, self.height)
        self.image_width = int(self.width / self.resize_scale)
        self.image_height = int(self.height / self.resize_scale)
        self.image_size = self.image_width * self.image_height
        pass

    # Take a screenshot
    # @return sct_img: An array containing the pixel values of the screenshot
    def take_screenshot(self):
        with mss.mss() as sct:
            sct_img = np.array(sct.grab(self.monitor))
        return sct_img

    # Set the necessary values for the monitoring area
    def set_coordinates(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.monitor = {"left": x, "top": y, "width": width, "height": height}
        self.image_size = {"x": int(width / self.resize_scale), "y": int(height / self.resize_scale)}

    # Get the size of the current image
    # @return image_size: A tuple containing the width and height of the current monitor area
    def get_image_size(self):
        return self.image_size

