from actions import action
import pyperclip


class Copy(action.Action):

    def __init__(self, target):
        self.target = target[0]
        # print("copy " + self.target)

    def execute(self, row):
        self.copy(row)

    def copy(self, row):
        print("Action: copy " + self.target + ". Copied value: " + row[self.target])
        pyperclip.copy(row[self.target])
