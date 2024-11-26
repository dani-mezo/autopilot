import pyautogui

from actions import action


class Scroll(action.Action):

    trigger = "scroll"

    def __init__(self, scroll):
        x, y, dx, dy = scroll
        self.x = int(x)
        self.y = int(y)
        self.dx = int(dx)
        self.dy = int(dy)

    def execute(self, row):
        self.scroll()

    def scroll(self):
        pyautogui.moveTo(self.x, self.y)
        if self.dy != 0:
            pyautogui.scroll(self.dy)
        if self.dx != 0:
            pyautogui.hscroll(self.dx)
        print(f"Action: scroll {self.x} {self.y} {self.dx} {self.dy}")

    @staticmethod
    def record(file, *data):
        x, y, dx, dy = data
        print(f"Scrolled at ({x}, {y}) with delta ({dx}, {dy})")
        file.write(f"{Scroll.trigger} {x} {y} {dx} {dy}\n")

