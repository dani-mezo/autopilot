import argparse
from configparser import ConfigParser
from actions.click import Click
from actions.copy import Copy
from actions.paste import Paste
from actions.wait import Wait
from data.data_reader import DataReader
from recorder.recorder import Recorder

actions = []
action_delimiter = ' '
action_types = {'click': Click, 'wait': Wait, 'copy': Copy, 'paste': Paste}
configuration_parser = ConfigParser()
initial_counter = 1


def read_actions(configuration):
    source = configuration['action_file_location']
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


def read_data(configuration):
    print('Reading up the data file.')
    data_reader = DataReader(configuration)
    return data_reader.read_structure()


def execute_actions(row):
    print("------------------------- Processing row")
    print(row)
    for action in actions:
        action.execute(row)


def record_mode(file_name):
    print("Recording mode has been activated.")
    recorder = Recorder(file_name)
    recorder.record()


def autopilot_mode():
    print("Autopilot mode has been activated.")
    configuration_parser.read('./config/configuration.txt')
    configuration = configuration_parser['Files']
    counter = read_actions(configuration)
    data = read_data(configuration)
    for index, row in data.iterrows():
        if index < counter - 1:
            pass
        else:
            execute_actions(row)


def run():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-r', type=bool, help='A flag to enable recordings of click points', default=False)
    parser.add_argument('--name', help='The name of the file that should be created with the recordings. When not provided,'
                                       'a random name will be generated for it.')
    args = parser.parse_args()

    if args.r:
        record_mode(args.name)
    else:
        autopilot_mode()


run()
