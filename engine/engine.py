from data.data_reader import DataReader
from time import sleep
import keyboard


class Engine:

    def __init__(self, configuration, counter, actions):
        self.configuration = configuration
        self.counter = counter
        self.actions = actions
        self.paused = True
        keyboard.add_hotkey('F2', lambda: self.pause())

    def execute(self):
        print("Initializing the execution of actions.")
        data = self.read_data()
        print("Paused. You may start or pause the execution with 'F2'.")
        for index, row in data.iterrows():
            if index < self.counter - 1:
                pass
            else:
                self.execute_actions(row)

    def read_data(self):
        print('Reading up the data file.')
        data_reader = DataReader(self.configuration)
        return data_reader.read_structure()

    def execute_actions(self, row):
        for action in self.actions:
            while self.paused:
                sleep(0.1)
            print("------------------------- Processing row")
            print(row)
            action.execute(row)

    def pause(self):
        self.paused = not self.paused


