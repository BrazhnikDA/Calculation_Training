import openpyxl
import pandas as pd

def importExcel(estimation):
    groups = []
    cal = []
    df = pd.DataFrame({'Наиминование':
                           [],
                       'Стоимость/Затраты':
                           []})
    df.to_excel('./teams.xlsx')
    filename = './teams.xlsx'
    wb = openpyxl.load_workbook(filename=filename)
    sheet = wb['Sheet1']
    for i in range(estimation.ListObject.__len__()):
        new_row = [i + 1, estimation.ListObject[i].Name,
                   int(int(estimation.ListObject[i].Salary) * int(estimation.ListObject[i].Count) / 22)]
        groups.append(estimation.ListObject[i].Name)
        cal.append(int(int(estimation.ListObject[i].Salary) * int(estimation.ListObject[i].Count) / 22))
        sheet.append(new_row)
    wb.save(filename)
    wb.close()