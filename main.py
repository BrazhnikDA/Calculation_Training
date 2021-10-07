from prettytable import PrettyTable  # Для отображения таблиц в консоли

from Information import Information  # Подключаем наш класс


# Отображение таблицы в консоль, на вход подаётся обьект класса Information
def CreateTable(info):
    th = ['Наименование', 'Количество', 'Стоимость/Затраты', 'Описание']
    td = []

    for i in range(info.ListObject.__len__()):
        td.append(info.ListObject[i].Name)
        td.append(info.ListObject[i].Count)
        td.append(info.ListObject[i].Salary)
        td.append(info.ListObject[i].Description)

    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    print(table)


def main():
    info = Information()
    info.Start()

    countLecturer = info.ListObject[0].Count
    salaryLecturer = info.ListObject[0].Salary

    print("Попробуем подсчитать примерную стоимость обучения в вузе.")
    print("За 6 лет программы обучения нам потребуется (учитывая все симестры) изучить n предметов.")
    print("Если взять, то что 1 преподаватель может вести 3 предмета, нам потруебся - ", countLecturer,
          "преподавателей")
    print("Средняя зарплата преподавателя по России - ", salaryLecturer)
    print("За 6 лет обучения это - ", salaryLecturer * 12 * 6 * countLecturer,
          "именно столько уйдёт на зарплату ", countLecturer, "преподавателям за 6 лет обучения")
    print("Теперь подсчитаем остальные затраты при оффлайн обучении: ")
    CreateTable(info)

    # На будущее
    # Построить график [x,y] где по x количество месяцев за 6 лет, по y сумма денег, нарисовать 2 линии потрачено и заработано при полном наборе предметов (онлайн,офлайн)
    # Добавить ещё 2 линии с тем сколько бы было потрачено, если бы предметы были только "нужные" по нашему мнению


if __name__ == '__main__':
    main()
