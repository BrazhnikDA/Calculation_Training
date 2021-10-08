import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
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
        td.append(int(estimation.ListObject[i].Salary/22)*int(estimation.ListObject[i].Count))
        if i == 0:
            continue
        rmp +=int(estimation.ListObject[i].Salary/22)*int(estimation.ListObject[i].Count)
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
    print("Попробуем подсчитать примерную стоимость оффлайн обучения в вузе.")
    print("За 6 лет программы обучения нам потребуется (учитывая все симестры) изучить n предметов.")
    print("Если взять, то что 1 преподаватель может вести 3 предмета, нам потруебся - ", countLecturer,
          "преподавателей")
    print("Средняя зарплата преподавателя по России - ", salaryLecturer)
    print("За 4 года обучения это - ", salaryLecturer * 12 * 4 * countLecturer,
          "именно столько уйдёт на зарплату ", countLecturer, "преподавателям за 6 лет обучения")
    print("Теперь подсчитаем остальные затраты в месяц при оффлайн обучении: ")
    CreateTable(info)
    print("А теперь подсчитаем сколько уходит на обучение одного студента:")
    estimation = info
    tmp        = CreateT(estimation)
    res        = int(salarySt - tmp)
    print("На столько переплачивает студент",res)
    print("На столько переплачивает группа студентов", res*22)
    groups = []
    cal    = []
    df = pd.DataFrame({'Наиминование':
                       [],
                       'Стоимость/Затраты':
                       []})
    df.to_excel('./teams.xlsx')
    filename = './teams.xlsx'
    wb = openpyxl.load_workbook(filename=filename)
    sheet = wb['Sheet1']
    for i in range(estimation.ListObject.__len__()):
        new_row = [i+1,estimation.ListObject[i].Name,int(int(estimation.ListObject[i].Salary)*int(estimation.ListObject[i].Count)/22)]
        groups.append(estimation.ListObject[i].Name)
        cal.append(int(int(estimation.ListObject[i].Salary)*int(estimation.ListObject[i].Count)/22))
        sheet.append(new_row)
    wb.save(filename)
    wb.close()

    print("\nСоставим уравнение сколько стоит весь процесс обучения")
    print("Все расходы в месяц умножить на 12 месяцев обучения и умножить на 4 года")
    sum = 0
    for i in range(info.ListObject.__len__() - 1):
        sum += (info.ListObject[i + 1].Salary * info.ListObject[i + 1].Count)

    print(sum, '* 12 * 4 = ', sum * 12 * 4)
    print("Доход от платных студентов за 4 года обучения")
    print("Стоимость обучения в месяц * 12 * количество студентов *  4")
    print(info.ListObject[0].Salary, " * 12 * ", info.ListObject[0].Count, " * 4 = ",
          info.ListObject[0].Salary * 12 * info.ListObject[0].Count * 4)

    '''
    plt.bar(groups,cal)
    #plt.show()
    vals = [24, 17, 53, 21, 35]
    labels = ["Ford", "Toyota", "BMV", "AUDI", "Jaguar"]
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels)
    ax.axis("equal")
    #plt.show()
'''
    fig, ax = plt.subplots()
    ax.pie(cal,labels=groups)
    ax.axis("equal")
    plt.show()

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

