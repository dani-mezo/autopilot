import string
import random
import keyboard
import sys
import mouse
import time
import calendar


class Recorder:

    def __init__(self, file_name):
        chars = string.ascii_lowercase
        if file_name is None:
            file_name = "./config/actions_" + ''.join(random.choice(chars) for x in range(5)) + '.txt'
        self.file_name = file_name
        self.file = open(file_name, 'w')
        self.first = True
        self.second = True
        self.mark = '--- MARKED FOR EDITION ---'
        self.stamp = 0
        self.file.write('repeat from row 1\n')

    def f2(self):
        print("Pressed 'F2'. Marking step in action file.")
        self.file.write(self.mark + '\n')

    def esc(self):
        print("Pressed 'ESC'. Ending all recordings.")
        self.file.close()
        mouse.unhook_all()
        sys.exit(1)

    def click(self):
        x, y = mouse.get_position()
        print("Click recorded. Position: " + str(x) + " " + str(y))
        if self.first:
            self.first = False
            pass
        else:
            fresh_stamp = calendar.timegm(time.gmtime())
            diff_seconds = fresh_stamp - self.stamp
            self.stamp = fresh_stamp
            if self.second:
                self.second = False
            else:
                print("Time difference recorded: " + str(diff_seconds))
                if diff_seconds > 0:
                    self.file.write("wait " + str(diff_seconds) + '\n')
            self.file.write("click " + str(x) + " " + str(y) + '\n')

    def init_log(self):
        print("Started recording into file: " + self.file_name)
        print("The very first click will be ignored. Press 'F2' if you want mark a step in the action file, and press"
              "'ESC' if you wish to end all recordings.")

    def record(self):
        self.init_log()
        mouse.on_click(self.click)
        keyboard.add_hotkey('F2', lambda: self.f2())
        keyboard.add_hotkey('ESC', lambda: self.esc())
        keyboard.wait()
