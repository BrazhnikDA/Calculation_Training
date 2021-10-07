import pandas as pd
import openpyxl
from prettytable import PrettyTable  # Для отображения таблиц в консоли
from Information import Information  # Подключаем наш класс

# Отображение таблицы в консоль, на вход подаётся обьект класса Information
def CreateTable(info):
    th = ['Наименование', 'Количество', 'Стоимость/Затраты','Описание']
    td = []

    for i in range(info.ListObject.__len__()):
        td.append(info.ListObject[i].Name)
        td.append(info.ListObject[i].Count)
        td.append(info.ListObject[i].Salary)
        #td.append(info.ListObject[i].Salary * 12* info.ListObject[i].Count)
        td.append(info.ListObject[i].Description)

    columns = len(th)
    table   = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    print(table)
#45 - зп в час
#1800 - часов
#'Траты в год'
def CreateT(estimation):
    th  = ['Наименование','Стоимость/Затраты']
    td  = []
    rmp = 0
    for i in range(estimation.ListObject.__len__()):
        td.append(estimation.ListObject[i].Name)
        td.append(int(estimation.ListObject[i].Salary/22))
        rmp = int(rmp + estimation.ListObject[i].Salary/22)
        # td.append(info.ListObject[i].Salary * 12* info.ListObject[i].Count)

    columns = len(th)
    table   = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    print(table)
    return rmp
def main():
    info = Information()
    info.Start()

    countLecturer  = info.ListObject[5].Count
    salaryLecturer = info.ListObject[5].Salary
    salarySt       = info.ListObject[0].Salary
    print("Попробуем подсчитать примерную стоимость обучения в вузе.")
    print("За 6 лет программы обучения нам потребуется (учитывая все симестры) изучить n предметов.")
    print("Если взять, то что 1 преподаватель может вести 3 предмета, нам потруебся - ", countLecturer,
          "преподавателей")
    print("Средняя зарплата преподавателя по России - ", salaryLecturer)
    print("За 6 лет обучения это - ", salaryLecturer * 12 * 6 * countLecturer,
          "именно столько уйдёт на зарплату ", countLecturer, "преподавателям за 6 лет обучения")
    print("Теперь подсчитаем остальные затраты при оффлайн обучении: ")
    CreateTable(info)
    print("А теперь подсчитаем сколько уходит на обучение одного студента:")
    estimation = info
    tmp        = CreateT(estimation)
    res        = int(salarySt - tmp)
    print("На столько переплачивает студент",res)
    print("На столько переплачивает группа студентов", res*22)
    df = pd.DataFrame({'Наиминование':
                       [],
                       'Стоимость/Затраты':
                       []})
    df.to_excel('./teams.xlsx')
    filename = './teams.xlsx'
    wb = openpyxl.load_workbook(filename=filename)
    sheet = wb['Sheet1']
    for i in range(estimation.ListObject.__len__()):
        new_row = [i+1,estimation.ListObject[i].Name,int(estimation.ListObject[i].Salary/22)]
        sheet.append(new_row)
    wb.save(filename)
    '''
    for i in range(estimation.ListObject.__len__()):
        td.append(estimation.ListObject[i].Name)
        td.append(int(estimation.ListObject[i].Salary / 22))
    td_data = td[:]
    columns = 2
    while td_data:
        df.add_row(td_data[:columns])
        td_data = td_data[columns:]
    '''


    # На будущее
    # Построить график [x,y] где по x количество месяцев за 6 лет, по y сумма денег, нарисовать 2 линии потрачено и заработано при полном наборе предметов (онлайн,офлайн)
    # Добавить ещё 2 линии с тем сколько бы было потрачено, если бы предметы были только "нужные" по нашему мнению


if __name__ == '__main__':
    main()

# info.ListObject[0].Name, info.ListObject[0].Count, info.ListObject[0].Salary, info.ListObject[0].Description,
#            info.ListObject[1].Name, info.ListObject[1].Count, info.ListObject[1].Salary, info.ListObject[1].Description,
#            info.ListObject[2].Name, info.ListObject[2].Count, info.ListObject[2].Salary, info.ListObject[2].Description,
#           info.ListObject[3].Name, info.ListObject[3].Count, info.ListObject[3].Salary, info.ListObject[3].Description,
#            info.ListObject[4].Name, info.ListObject[4].Count, info.ListObject[4].Salary, info.ListObject[4].Description,
#            info.ListObject[5].Name, info.ListObject[5].Count, info.ListObject[5].Salary, info.ListObject[5].Description,
#            info.ListObject[6].Name, info.ListObject[6].Count, info.ListObject[6].Salary, info.ListObject[6].Description,
#            info.ListObject[7].Name, info.ListObject[7].Count, info.ListObject[7].Salary, info.ListObject[7].Description
