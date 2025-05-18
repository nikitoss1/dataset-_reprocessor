import unittest
from model.load_data import LoadData

class TestDefineSep(unittest.TestCase):

    def test_exist_file(self):
        path = '/home/nikitoss/Рабочий стол/diploma/tests/datasets/data_comma.csv'
        load_data = LoadData(path)
        self.assertEqual(load_data.check_existence_of_dataset(), True)

    def test_not_exist_file(self):
        path = '/home/nikitoss/Рабочий стол/diploma/tests/datasets/data_comma46.csv'
        load_data = LoadData(path)
        self.assertEqual(load_data.check_existence_of_dataset(), False)
if __name__ == '__main__':
    unittest.main()