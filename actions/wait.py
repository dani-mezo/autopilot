from actions import action
from time import sleep


class Wait(action.Action):

    def __init__(self, duration_seconds):
        self.duration_seconds = int(duration_seconds[0])
        # print('wait ' + str(self.duration_seconds))

    def execute(self, row):
        self.wait()

    def wait(self):
        print('Action: wait ' + str(self.duration_seconds) + " seconds")
        sleep(self.duration_seconds)
