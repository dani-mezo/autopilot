from actions import action
from pynput.keyboard import Key, Controller


class Paste(action.Action):

    def __init__(self, args):
        # print("paste")
        pass

    def execute(self, row):
        self.paste()

    def paste(self):
        print("Action: paste")
        keyboard = Controller()
        keyboard.press(Key.ctrl_l.value)
        keyboard.press('v')
        keyboard.release(Key.ctrl_l.value)
        keyboard.release('v')
