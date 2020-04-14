import time
import keyboard


# Records all initialised input used by the user
class InputListener:
    def __init__(self):
        self.set_key_events()
        self.keys_pressed_down = []

    # Add listeners to the desired keys
    def set_key_events(self):
        self.add_key_events("up")
        self.add_key_events("down")
        self.add_key_events("left")
        self.add_key_events("right")
        self.add_key_events("space")
        self.add_key_events("q")
        self.add_key_events("z")
        self.add_key_events("x")

    # Add a key to the list of pressed keys if not already present
    def add_key_to_list(self, key):
        if key not in self.keys_pressed_down:
            self.keys_pressed_down.append(key)

    # Remove a key from the list of pressed keys
    def remove_key_from_list(self, key):
        if key in self.keys_pressed_down:
            self.keys_pressed_down.remove(key)

    # Empty the key list
    def clear_key_list(self):
        self.keys_pressed_down = []

    # Get the list of pressed keys
    # @return key_pressed_down: A list containing all keys pressed since the last clear
    def get_keys_pressed_down(self):
        return self.keys_pressed_down

    # Add a listener to a specific keyboard key
    def add_key_events(self, key):
        keyboard.on_press_key(key, lambda _: self.add_key_to_list(key))
        keyboard.on_release_key(key, lambda _: self.remove_key_from_list(key))
