import win32api, win32con
from win32api import GetSystemMetrics
from actions import action


class Click(action.Action):

    def __init__(self, point):
        x, y = point
        self.x = int(x)
        self.y = int(y)
        # print("click " + str(self.x) + " " + str(self.y))

    def execute(self, row):
        self.click()

    def click(self):
        print("Action: click " + str(self.x) + " " + str(self.y))
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(self.x/GetSystemMetrics(0) * 65535.0), int(self.y/GetSystemMetrics(1) * 65535.0))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.x, self.y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.x, self.y, 0, 0)
