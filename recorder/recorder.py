import random
import string
import sys

from pynput import mouse, keyboard

from actions.click import Click
from actions.key_down import KeyDown
from actions.key_up import KeyUp
from actions.scroll import Scroll


class Recorder:

    def __init__(self, file_name):
        chars = string.ascii_lowercase
        if file_name is None:
            file_name = "./config/actions_" + ''.join(random.choice(chars) for x in range(5)) + '.txt'
        self.file_name = file_name
        self.file = open(file_name, 'w')
        self.first = True
        self.second = True
        self.mark = '--- MARKED FOR EDITION ---'
        self.stamp = 0
        self.file.write('repeat from row 1\n')
        self.mouse_listener = None
        self.keyboard_listener = None

    def pause(self):
        print("Pressed 'Pause'. Marking step in action file.")
        self.file.write(self.mark + '\n')

    def esc(self):
        print("Pressed 'ESC'. Ending all recordings.")
        self.file.write('esc')
        self.file.close()
        if self.mouse_listener:
            self.mouse_listener.stop()
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        sys.exit(1)

    def init_log(self):
        print(f"Started recording into file: {self.file_name}")
        print("The very first click will be ignored. Press 'Pause' if you want to mark a step in the action file, and "
              "press 'ESC' if you wish to end all recordings.")

    def record(self):
        self.init_log()

        def on_press(key):
            if key == keyboard.Key.pause:
                self.pause()
            elif key == keyboard.Key.esc:
                self.esc()
            else:
                KeyDown.record(self.file, key)

        def on_click(x, y, button, pressed):
            if pressed:
                Click.record(self.file, button)

        def on_scroll(x, y, dx, dy):
            Scroll.record(self.file, x, y, dx, dy)

        def on_release(key):
            if key == keyboard.Key.pause or key == keyboard.Key.esc:
                pass
            KeyUp.record(self.file, key)

        if not self.mouse_listener:
            self.mouse_listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
            self.mouse_listener.start()

        if not self.keyboard_listener:
            self.keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
            self.keyboard_listener.start()

        self.mouse_listener.join()
        self.keyboard_listener.join()
