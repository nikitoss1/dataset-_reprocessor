import unittest
from model.load_data import DefineDf
from config.constants import DIR

class TestDefineSep(unittest.TestCase):

    def test_comma(self):
        load_data = DefineDf(f'{DIR}tests/datasets/data_comma.csv')
        sep = load_data.define_sep()
        self.assertEqual(',', sep)


    def test_semicolon(self):
        load_data = DefineDf(f'{DIR}tests/datasets/data_semicolon.csv')
        sep = load_data.define_sep()
        self.assertEqual(';', sep)


    def test_tab(self):
        load_data = DefineDf(f'{DIR}tests/datasets/data_tab.tsv')
        sep = load_data.define_sep()
        self.assertEqual('\t', sep)


    def test_space(self):
        load_data = DefineDf(f'{DIR}tests/datasets/data_space.txt')
        sep = load_data.define_sep()
        self.assertEqual(' ', sep)


    def test_colon(self):
        load_data = DefineDf(f'{DIR}tests/datasets/data_colon.txt')
        sep = load_data.define_sep()
        self.assertEqual(':', sep)

    def test_lattice(self):
        load_data = DefineDf(f'{DIR}tests/datasets/data_lattice.txt')
        sep = load_data.define_sep()
        self.assertEqual('#', sep)

    def test_tilda(self):
        load_data = DefineDf(f'{DIR}tests/datasets/data_tilda.txt')
        sep = load_data.define_sep()
        self.assertEqual('~', sep)

    def test_caret(self):
        load_data = DefineDf(f'{DIR}tests/datasets/data_caret.txt')
        sep = load_data.define_sep()
        self.assertEqual('^', sep)

    def test_none(self):
        load_data = DefineDf(f'{DIR}tests/datasets/data_example6.csv')
        sep = load_data.define_sep()
        self.assertEqual(None, sep)

if __name__ == '__main__':
    unittest.main()