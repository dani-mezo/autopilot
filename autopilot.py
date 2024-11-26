import argparse
from configparser import ConfigParser
from actions.click import Click
from actions.combo import Combo
from actions.copy import Copy
from actions.esc import Escape
from actions.key_up import KeyUp
from actions.paste import Paste
from actions.key_down import KeyDown
from actions.scroll import Scroll
from actions.wait import Wait
from engine.engine import Engine
from recorder.recorder import Recorder

actions = []
action_delimiter = ' '
action_types = {action.trigger: action for action in [Click, Wait, Copy, Paste, KeyDown, KeyUp, Scroll, Escape, Combo]}
configuration_parser = ConfigParser()
initial_counter = 1


def read_actions(source):
    source = f"./config/actions_{source}.txt" if not source.startswith("./config/actions_") else source
    print('Reading up action configuration from source: ' + source)
    actions_configuration = open(source, 'r')
    for action in actions_configuration:
        raw_action = action.replace('\n', '').replace('\r', '')
        if raw_action.startswith('repeat'):
            initial_counter = raw_action.split(' ')[-1]
        else:
            actions.append(create_action(raw_action))
    return int(initial_counter)


def create_action(action):
    action_parameters = action.split(action_delimiter)
    try:
        action_type = action_parameters[0]
        action_class = action_types[action_type]
    except KeyError as e:
        print('Check your action configuration. Upon processing line "' + action + '", found error:')
        print(repr(e))
        exit(1)
    action = action_class(action_parameters[1:])
    return action


def record_mode(file_name):
    print("Recording mode has been activated.")
    recorder = Recorder(file_name)
    recorder.record()


def autopilot_mode(file_name):
    print("Autopilot mode has been activated.")
    configuration_parser.read('./config/configuration.txt')
    configuration = configuration_parser['Files']
    counter = read_actions(file_name)
    engine = Engine(configuration, counter, actions)
    engine.execute()


def run():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--record', action='store_true', help='Enable recording mode to record GUI actions')
    parser.add_argument('--target', help='The name of the target file that should be created with the '
                                         'recordings or executed by autopilot. When not provided '
                                         'a random name will be generated for it in recording mode.')
    args = parser.parse_args()

    if args.record:
        record_mode(args.target)
    else:
        autopilot_mode(args.target)


run()
