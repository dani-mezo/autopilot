import sys

from actions import action


class Escape(action.Action):

    trigger = "esc"

    def __init__(self, key):
        self.key = key

    def execute(self, row):
        sys.exit()

    @staticmethod
    def record(file, *data):
        pass