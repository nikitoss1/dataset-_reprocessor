import unittest
import pandas as pd
import os
from model.export_data import ExportData
from config.constants import DIR
from config.format import Format

class TestExportData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.export_dir = os.path.join(DIR, 'exporting_datasets')
        os.makedirs(cls.export_dir, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        for filename in os.listdir(cls.export_dir):
            file_path = os.path.join(cls.export_dir, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Ошибка при удалении {file_path}: {e}")

    def test_export_to_csv(self):
        test_filename = 'test_export.csv'
        expected_path = os.path.join(self.export_dir, test_filename)
        
        df = pd.read_csv(os.path.join(DIR, 'tests/datasets/data_example3.csv'))
        
        ExportData(df, Format.CSV, 'test_export')
        
        self.assertTrue(os.path.exists(expected_path), 
                       f"Файл {expected_path} не был создан")
        
        exported_df = pd.read_csv(expected_path)
        pd.testing.assert_frame_equal(df, exported_df)

    def test_export_to_tsv(self):
        test_filename = 'test_export2.tsv'
        expected_path = os.path.join(self.export_dir, test_filename)
        
        df = pd.read_csv(os.path.join(DIR, 'tests/datasets/data_tab.tsv'), sep='\t')
        
        ExportData(df, Format.TSV, 'test_export2')
        
        self.assertTrue(os.path.exists(expected_path), 
                       f"Файл {expected_path} не был создан")
        
        exported_df = pd.read_csv(expected_path, sep='\t')
        pd.testing.assert_frame_equal(df, exported_df)

    def test_export_to_txt(self):
        test_filename = 'test_export3.txt'
        expected_path = os.path.join(self.export_dir, test_filename)
        
        df = pd.read_csv(os.path.join(DIR, 'tests/datasets/data_tilda.txt'), sep='~')
        
        ExportData(df, Format.TXT, 'test_export3')
        
        self.assertTrue(os.path.exists(expected_path), 
                       f"Файл {expected_path} не был создан")
        
        exported_df = pd.read_csv(expected_path, sep=';')
        pd.testing.assert_frame_equal(df, exported_df)

    def test_export_to_excel(self):
        test_filename = 'test_export4.xlsx'
        expected_path = os.path.join(self.export_dir, test_filename)
        
        df = pd.read_excel(os.path.join(DIR, 'tests/datasets/data_excel.xlsx'))
        
        ExportData(df, Format.XLSX, 'test_export4')
        
        self.assertTrue(os.path.exists(expected_path), 
                       f"Файл {expected_path} не был создан")
        

if __name__ == '__main__':
    unittest.main()