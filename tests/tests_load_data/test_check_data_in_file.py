import unittest
from model.load_data import DefineDf
from config.constants import DIR

class TestDefineSep(unittest.TestCase):

    def test_normal_data1(self):
        path = f'{DIR}tests/datasets/data_example1.csv'
        load_data = DefineDf(path)
        self.assertEqual(load_data.check_data_in_file(), True)

    def test_normal_data2(self):
        path = f'{DIR}tests/datasets/data_example2.csv'
        load_data = DefineDf(path)
        self.assertEqual(load_data.check_data_in_file(), True)

    def test_normal_data3(self):
        path = f'{DIR}tests/datasets/data_example3.csv'
        load_data = DefineDf(path)
        self.assertEqual(load_data.check_data_in_file(), True)

    def test_normal_data4(self):
        path = f'{DIR}tests/datasets/data_example4.csv'
        load_data = DefineDf(path)
        self.assertEqual(load_data.check_data_in_file(), True)

    def test_bad_data1(self):
        path = f'{DIR}tests/datasets/data_example5.csv'
        load_data = DefineDf(path)
        self.assertEqual(load_data.check_data_in_file(), False)

    def test_bad_data2(self):
        path = f'{DIR}tests/datasets/data_example6.csv'
        load_data = DefineDf(path)
        self.assertEqual(load_data.check_data_in_file(), False)



        
if __name__ == '__main__':
    unittest.main()