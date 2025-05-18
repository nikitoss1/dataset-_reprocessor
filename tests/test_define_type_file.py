import unittest
from model.load_data import LoadData

class TestDefineTypeFile(unittest.TestCase):
    
    def test_csv(self):
        load_data = LoadData('dataset/churn.csv')
        type_file = load_data.define_type_file()
        self.assertEqual('csv', type_file)

    def test_tsv(self):
        load_data = LoadData('dataset/churn.tsv')
        type_file = load_data.define_type_file()
        self.assertEqual('tsv', type_file)

    def test_txt(self):
        load_data = LoadData('dataset/ex1data1.txt')
        type_file = load_data.define_type_file()
        self.assertEqual('txt', type_file)

    def test_xlsx(self):
        load_data = LoadData('datasets/data_excel.xlsx')
        type_file = load_data.define_type_file()
        self.assertEqual('xlsx', type_file)

    def test_xls(self):
        load_data = LoadData('datasets/data_excel.xls')
        type_file = load_data.define_type_file()
        self.assertEqual('xls', type_file)

    def test_xlsm(self):
        load_data = LoadData('datasets/data_excel.xlsm')
        type_file = load_data.define_type_file()
        self.assertEqual('xlsm', type_file)

    def test_xlsb(self):
        load_data = LoadData('datasets/data_excel.xlsb')
        type_file = load_data.define_type_file()
        self.assertEqual('xlsb', type_file)

if __name__ == '__main__':
    unittest.main()