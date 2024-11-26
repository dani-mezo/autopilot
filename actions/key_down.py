import pyautogui
from actions import action
from actions.keys import Keys


class KeyDown(action.Action):

    trigger = "keydown"

    def __init__(self, key):
        self.key = key

    def execute(self, row):
        self.press_key()

    def press_key(self):
        print(f"Action: key down {self.key}")
        for key in self.key:
            pyautogui.keyDown(key)

    @staticmethod
    def record(file, key):
        if Keys.get_key(key):
            print(f"Key kept down recorded: {key}")
        else:
            print(f"Key down recorded: {key}")
        file.write(f"{KeyDown.trigger} {key}\n")