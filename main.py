from prettytable import PrettyTable  # Для отображения таблиц в консоли
from Information import Information

def CreateTable(info):
    th = ['Наименование', 'Затраты', 'Описание']
    td = \
        [
            '1', '2', '3',
            'b', '2', '3',
            'c', '2', '3',
            'd', 'ddddddddd', '33333333333333333333'
        ]

    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    print(table)


def main():
    info = Information()

    print("Попробуем подсчитать примерную стоимость обучения в вузе.")
    print("За 6 лет программы обучения нам потребуется (учитывая все симестры) изучить n предметов.")
    print("Если взять, то что 1 преподаватель может вести 3 предмета, нам потруебся - ",
          info.countLecturer, "преподавателей")
    print("Средняя зарплата преподавателя по России - ", info.lecturerCost)
    print("За 6 лет обучения это - ", info.lecturerCost * 12 * 6 * info.countLecturer,
          "именно столько уйдёт на зарплату ", info.countLecturer, "преподавателям за 6 лет обучения")
    print("Теперь подсчитаем остальные затраты при оффлайн обучении: ")
    CreateTable(info)
    # Построить график [x,y] где по x количество месяцев за 6 лет, по y сумма денег, нарисовать 2 линии потрачено и заработано при полном наборе предметов (онлайн,офлайн)
    # Добавить ещё 2 линии с тем сколько бы было потрачено, если бы предметы были только "нужные" по нашему мнению


if __name__ == '__main__':
    main()
