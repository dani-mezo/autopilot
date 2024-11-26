import pyautogui
from actions import action
from actions.keys import Keys


class KeyUp(action.Action):

    trigger = "keyup"

    def __init__(self, key):
        self.key = key

    def execute(self, row):
        self.release_keys()

    def release_keys(self):
        print(f"Action: key up {self.key}")
        for key in self.key:
            pyautogui.keyUp(key)

    @staticmethod
    def record(file, key):
        print(f"Key up recorded: {key}")
        Keys.add_key(key)
        file.write(f"{KeyUp.trigger} {key}\n")