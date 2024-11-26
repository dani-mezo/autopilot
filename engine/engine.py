from itertools import cycle

from pynput import keyboard

from data.data_reader import DataReader


class Engine:

    exit_flag = False

    def __init__(self, configuration, counter, actions):
        self.configuration = configuration
        self.counter = counter
        self.actions = actions
        self.paused = True

    @staticmethod
    def on_esc(key):
        if key == keyboard.Key.esc:
            Engine.exit_flag = True
            return False

    def execute(self):
        print("Initializing the execution of actions.")
        # data = self.read_data()
        print("Paused. You may start or pause the execution with 'Pause'.")
        actions_iterator = cycle(self.actions)
        with keyboard.Listener(on_press=Engine.on_esc) as listener:
            while not Engine.exit_flag:
                next(actions_iterator).execute(None)

    def read_data(self):
        print('Reading up the data file.')
        data_reader = DataReader(self.configuration)
        return data_reader.read_structure()

    def pause(self):
        self.paused = not self.paused
