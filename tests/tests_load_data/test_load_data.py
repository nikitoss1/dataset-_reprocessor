import unittest
from model.load_data import LoadData, NotDatasetError, DefineDf
import pandas as pd
from config.constants import DIR

class TestDefineTypeFile(unittest.TestCase):
    
    def test_load_csv(self):
        df_true = pd.read_csv(f'{DIR}tests/datasets/data_example3.csv')
        df_test = LoadData(f'{DIR}tests/datasets/data_example3.csv').df

        result = df_true.equals(df_test)
        self.assertEqual(result, True)

    def test_load_tsv(self):
        df_true = pd.read_csv(f'{DIR}tests/datasets/data_tab.tsv', sep='\t')
        df_test = LoadData(f'{DIR}tests/datasets/data_tab.tsv').df

        result = df_true.equals(df_test)
        self.assertEqual(result, True)

    def test_load_txt(self):
        df_true = pd.read_csv(f'{DIR}tests/datasets/ex1data1.txt')
        df_test = LoadData(f'{DIR}tests/datasets/ex1data1.txt').df

        result = df_true.equals(df_test)
        self.assertEqual(result, True)

    def test_load_excel(self):
        df_true = pd.read_excel(f'{DIR}tests/datasets/data_excel.xls')
        df_test = LoadData(f'{DIR}tests/datasets/data_excel.xls').df

        result = df_true.equals(df_test)
        self.assertEqual(result, True)

    def test_load_bad_data(self):
        try:
            LoadData(f'{DIR}tests/datasets/data_example5.csv')
        except NotDatasetError as e:
            self.assertEqual(True, True)
            return
        
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()