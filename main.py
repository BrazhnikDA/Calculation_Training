import os

import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table
from prettytable import PrettyTable  # Для удобного отображения таблиц в консоли

from ImportExcel import importExcel  # Подключаем функцию и файла для вывода в Excel
from Information import Information  # Подключаем наш класс


# Отображение таблицы в консоль, на вход подаётся обьект класса Information
def CreateTable(info):
    th = ['Наименование', 'Количество', 'Стоимость/Затраты', 'Описание']
    td = []

    for i in range(info.ListObject.__len__()):
        td.append(info.ListObject[i].Name)
        td.append(info.ListObject[i].Count)
        td.append(info.ListObject[i].Salary)
        # td.append(info.ListObject[i].Salary * 12* info.ListObject[i].Count)
        td.append(info.ListObject[i].Description)

    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    print(table)


def CheckPayMonth(res):
    if (res > 0):
        print("На столько переплачивает студент - ", abs(res))
        print("На столько переплачивает группа студентов - ", abs(res * 22))
    else:
        print("Столько не доплачивает студент - ", abs(res))
        print("Столько не доплачивает группа студентов - ", abs(res * 22))


def CreateLinearEquation(type):
    print("\nСоставим уравнение сколько стоит весь процесс обучения")
    print("Все расходы в месяц умножить на 12 месяцев обучения и умножить на 4 года")
    month = 0
    for i in range(type.ListObject.__len__() - 1):
        month += (type.ListObject[i + 1].Salary * type.ListObject[i + 1].Count)

    print(month, '* 12 * 4 = ', month * 12 * 4)
    print("Доход от платных студентов за 4 года обучения")
    print("Стоимость обучения в месяц * 12 * количество студентов *  4")
    print(type.ListObject[0].Salary, "* 12 * ", type.ListObject[0].Count, " * 4 =",
          type.ListObject[0].Salary * 12 * type.ListObject[0].Count * 4)

    return month * 12 * 4


def CreateChart(num, groups, title):
    th = ['Name', 'Salary']
    td = {
        'Name': [],
        'Salary': []
    }
    for i in range(num.__len__()):
        td['Name'].append(groups[i])
        td['Salary'].append(num[i])

    df = pd.DataFrame(td, columns=th)

    ax1 = plt.subplot(121, aspect='equal')
    df.plot(kind='pie', y='Salary', ax=ax1, autopct='%1.1f%%', startangle=0, shadow=False, labels=df['Name'],
            legend=False, fontsize=8)
    plt.legend(loc=2, prop={'size': 5})
    ax2 = plt.subplot(122)
    plt.axis('off')
    tbl = table(ax2, df, loc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    plt.savefig('This_is_diagramme.jpg')
    plt.show()


# plt.savefig('This_is_diagramme.jpg')
def CreateT(estimation):
    th = ['Наименование', 'Стоимость/Затраты']
    td = []
    rmp = 0
    for i in range(estimation.ListObject.__len__()):
        td.append(estimation.ListObject[i].Name)
        td.append(int(estimation.ListObject[i].Salary / 22) * int(estimation.ListObject[i].Count))
        if i == 0:
            continue
        rmp += int(estimation.ListObject[i].Salary / 22) * int(estimation.ListObject[i].Count)
        # td.append(info.ListObject[i].Salary * 12* info.ListObject[i].Count)

    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    print(table)
    return rmp


# Проверка на доступ к папке (параметр - путь до папки)
# проверка существования файла или каталога,
# проверка возможности чтения,
# проверка открытия директории
def checkAccessFolder(_path):
    __file__ = _path
    if os.access(__file__, os.F_OK) == False:
        return False
    if os.access(__file__, os.R_OK) == False:
        return False
    if os.access(__file__, os.X_OK) == False:
        return False

    return True


def main():
    if checkAccessFolder(os.getcwd() + "\\offline.json") == False:
        print('Нет доступа к ' + os.getcwd() + "\\offline.json")
        if checkAccessFolder(os.getcwd() + "\\online.json") == False:
            print('Нет доступа к ' + os.getcwd() + "\\online.json")
        return

    offline = Information()
    offline.Start(os.getcwd() + "\\offline.json")

    countLecturer = offline.ListObject[5].Count
    salaryLecturer = offline.ListObject[5].Salary
    salarySt = offline.ListObject[0].Salary

    print("Попробуем подсчитать примерную стоимость оффлайн обучения в вузе.")
    print("За 4 года программы обучения нам потребуется (учитывая все симестры) изучить n предметов.")
    print("Если взять, то что 1 преподаватель может вести 3 предмета, нам потруебся - ", countLecturer,
          "преподавателей")
    print("Средняя зарплата преподавателя по России - ", salaryLecturer)
    print("За 4 года обучения это - ", salaryLecturer * 12 * 4 * countLecturer,
          "именно столько уйдёт на зарплату ", countLecturer, "преподавателям за 4 года обучения")

    print("Теперь подсчитаем остальные затраты в месяц при оффлайн обучении: ")
    CreateTable(offline)

    print("А теперь подсчитаем сколько уходит на обучение одного студента:")
    tmp = CreateT(offline)
    resOff = int(salarySt - tmp)
    CheckPayMonth(resOff)

    print("Импортируем вторую таблицу в Excel")
    importExcel(offline)

    sumOff = CreateLinearEquation(offline)

    groups = []
    cal = []
    for i in range(offline.ListObject.__len__()):
        groups.append(offline.ListObject[i].Name)
        cal.append(int(int(offline.ListObject[i].Salary) * int(offline.ListObject[i].Count) / 22))

    CreateChart(cal, groups, 'Диаграмма затрат на обучение')

    offline.ListObject.clear()  # Отчистим список с уже имеющимися данными

    print("\n\nСделаем расчёт для онлайн обучения вычеркнув по нашему мнению, не очень нужные предметы")
    online = Information()
    online.Start(os.getcwd() + "\\online.json")
    CreateTable(online)

    print("А теперь подсчитаем сколько уходит на обучение одного студента, но уже онлайн:")
    tmp = CreateT(online)
    resOn = int(online.ListObject[0].Salary - tmp)
    CheckPayMonth(resOn)

    sumOn = CreateLinearEquation(online)

    print("\nПодведём итоги!")

    if sumOn < sumOff:
        print("Обучение онлайн дешевле обходится вузу на - ", sumOff - sumOn)
    else:
        print("Обучение оффлайн дешевле обходится вузу на - ", sumOn - sumOff)
    print("За 4 года обучения")


if __name__ == '__main__':
    main()
