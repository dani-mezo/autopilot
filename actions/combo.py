import pyautogui

from actions import action


class Combo(action.Action):

    trigger = "combo"

    def __init__(self, keys):
        self.keys = keys

    def execute(self, row):
        pyautogui.hotkey(*self.keys)

    @staticmethod
    def record(file, *data):
        pass