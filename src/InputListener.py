import time
import keyboard


class InputListener:
    def __init__(self):
        self.set_key_events()
        self.keys_pressed_down = []

    def set_key_events(self):
        self.add_key_events("up")
        self.add_key_events("down")
        self.add_key_events("left")
        self.add_key_events("right")
        self.add_key_events("space")

    def add_key_to_list(self, key):
        if key not in self.keys_pressed_down:
            self.keys_pressed_down.append(key)

    def remove_key_from_list(self, key):
        if key in self.keys_pressed_down:
            self.keys_pressed_down.remove(key)

    def get_keys_pressed_down(self):
        return self.keys_pressed_down

    def add_key_events(self, key):
        keyboard.on_press_key(key, lambda _: self.add_key_to_list(key))
        keyboard.on_release_key(key, lambda _: self.remove_key_from_list(key))
