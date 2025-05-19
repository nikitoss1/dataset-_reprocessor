import pandas as pd
from config.format import Format
from config.constants import DIR

class ExportData:

    def __init__(self, df: pd.DataFrame, format: Format=Format.CSV, name_file='output'):
        if format == Format.CSV:
            df.to_csv(f'{DIR}exporting_datasets/{name_file}.csv', index=False, encoding='utf-8')
        elif format == Format.TSV:
            df.to_csv(f'{DIR}exporting_datasets/{name_file}.tsv', sep='\t', index=False, encoding='utf-8')
        elif format == Format.TXT:
            df.to_csv(f'{DIR}exporting_datasets/{name_file}.txt', sep=';', index=False, encoding='utf-8')
        elif format == Format.XLSX:
            df.to_excel(f'{DIR}exporting_datasets/{name_file}.xlsx', index=False, engine='openpyxl')
        elif format == Format.XLS:
            df.to_excel(f'{DIR}exporting_datasets/{name_file}.xls', index=False, engine='xlwt')
        elif format == Format.XLSM:
            df.to_excel(f'{DIR}exporting_datasets/{name_file}.xlsm', index=False, engine='xlsxwriter')

if __name__ == "__main__":
    df = pd.read_csv(f'{DIR}tests/datasets/data_example1.csv')
    print(df)
    ExportData(df)
