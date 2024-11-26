import calendar
import time

import pyautogui
from actions import action


class Click(action.Action):

    first_click = True
    second_click = False
    stamp = None
    trigger = "click"

    def __init__(self, click):
        x, y, button = click
        self.x = int(x)
        self.y = int(y)
        self.button = button

    def execute(self, row):
        self.click()

    def click(self):
        print(f"Action: click {self.x} {self.y}")
        pyautogui.click(x=self.x, y=self.y, button=self.button)

    @staticmethod
    def record(file, button):
        x, y = pyautogui.position()
        button_type = str(button).replace('Button.', '')
        print(f"Click recorded. Position: {x} {y}. Button: {button_type}")
        if Click.first_click:
            Click.first_click = False
            Click.second_click = True
            Click.stamp = calendar.timegm(time.gmtime())
            return
        fresh_stamp = calendar.timegm(time.gmtime())
        diff_seconds = fresh_stamp - Click.stamp
        Click.stamp = fresh_stamp
        if Click.second_click:
            Click.second_click = False
        else:
            print(f"Time difference recorded: {diff_seconds}")
            if diff_seconds > 0:
                file.write(f"wait {diff_seconds}\n")
        file.write(f"{Click.trigger} {x} {y} {button_type}\n")
