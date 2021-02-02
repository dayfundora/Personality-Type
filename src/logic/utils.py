import pandas as pd

def write_to_xlsx(dataframe, columns_names, rows_names, xlsx_name):
    writer = pd.ExcelWriter(xlsx_name, engine='xlsxwriter')
    dataframe.to_excel(writer, sheet_name='Sheet1')
    writer.save()

