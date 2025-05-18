import pandas as pd
import csv


class LoadData:

    def __init__(self, path: str, first_str_is_header=True):
        self.path = path


    def check_existence_of_dataset(self):
        try:
            with open(self.path, "r", encoding='utf-8'):
                pass
            return True
        except FileNotFoundError as e:
            self.path = None
            return False

    def define_sep(self):
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                sample = file.read(2048)
            dialect = csv.Sniffer().sniff(sample)
            return dialect.delimiter
        except Exception as e:
            return None

    def define_type_file(self):
        return self.path.split(".")[-1]

    def check_data_in_file(self):
        if self.define_sep():
            return True
        else:
            return False


    def create_df(self):
        if self.type == 'csv' or self.type == 'tsv' or self.type == 'txt':
            self.df = pd.read_csv(self.path)
        else:
            self.df = pd.read_excel(self.path)