import pandas as pd


class DataReader:

    def __init__(self, configuration):
        self.file = configuration['data_file_location']
        self.sheet = configuration['data_file_sheet']

    def read_structure(self):
        data = pd.read_excel(self.file, sheet_name=self.sheet)
        return data
