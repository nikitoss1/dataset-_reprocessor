import pandas as pd
import csv
import os

class NotDatasetError(Exception):
    pass

class DefineDf:
    def __init__(self, path: str, first_str_is_header=True):
        self.path = path
        self.sep = None
        self._df = None  # Приватный атрибут
        self.first_str_is_header = first_str_is_header
        self._type = self.define_type_file()  # Приватный атрибут
    
    @property
    def df(self):
        return self._df
    
    @df.setter
    def df(self, value):
        self._df = value
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, value):
        self._type = value

    def check_existence_of_dataset(self):
        return os.path.exists(self.path)

    def check_data_in_file(self):
        return self.define_sep() is not None

    def define_sep(self):
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                sample = file.read(2048)
            self.sep = csv.Sniffer().sniff(sample).delimiter
            return self.sep
        except Exception:
            return None

    def define_type_file(self):
        return self.path.split(".")[-1].lower()

    def create_df(self):
        self._type = self.define_type_file()
        
        if self._type in ["csv", "tsv", "txt"]:
            # Определяем разделитель
            sep = self.define_sep()
            
            if self.first_str_is_header:
                # Если есть заголовок
                self._df = pd.read_csv(self.path, sep=sep, header=0)
            else:
                # Если заголовка нет, читаем первую строку для определения числа столбцов
                df_temp = pd.read_csv(self.path, sep=sep, header=None, nrows=1)
                num_columns = df_temp.shape[1]  # Количество столбцов
                names = [f'col_{i}' for i in range(num_columns)]  # Генерируем имена
                self._df = pd.read_csv(self.path, sep=sep, header=None, names=names)
        
        else:  # Для Excel
            if self.first_str_is_header:
                self._df = pd.read_excel(self.path, header=0)
            else:
                df_temp = pd.read_excel(self.path, header=None, nrows=1)
                num_columns = df_temp.shape[1]
                names = [f'col_{i}' for i in range(num_columns)]
                self._df = pd.read_excel(self.path, header=None, names=names)

class LoadData(DefineDf):
    def __init__(self, path, first_str_is_header=True):
        super().__init__(path, first_str_is_header)
        self.types_with_sep = ["csv", "tsv", "txt"]
        try:
            self.control_data()
            self.create_df()
        except (FileNotFoundError, NotDatasetError) as e:
            raise

    def control_data(self):
        if not self.check_existence_of_dataset():
            raise FileNotFoundError("File not found")        
        if self.type in self.types_with_sep and not self.check_data_in_file():
            raise NotDatasetError("This file is not a dataset")

if __name__ == "__main__":
    ld = LoadData('/home/nikitoss/Рабочий стол/diploma/tests/datasets/data_colon.txt', first_str_is_header=False)
    print(ld.df)  # Используйте ld.df, а не ld.get_df