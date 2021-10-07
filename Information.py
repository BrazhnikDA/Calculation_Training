import pandas as pd             # Для работы с JSON
from ObjectJson import Object   # Класс описывающий модель

class Information:
    # создание списка хранящий массив записей из JSON
    ListObject = []

    # Геттеры
    def getName(self, index):
        obj = self.ListObject[index]
        return obj.__getitem__(Object, 0)

    def getCount(self, index):
        obj = self.ListObject[index]
        return obj.__getitem__(Object, 1)

    def getSalary(self, index):
        obj = self.ListObject[index]
        return obj.__getitem__(Object, 2)

    def getDescription(self, index):
        obj = self.ListObject[index]
        return obj.__getitem__(Object, 3)

    # Спарсить данные с файла json, если ошибка выкидываем exception
    def ParseJson(self):
        try:
            patients_df = pd.read_json("C:\\offline2.json")
            patients_df.head()
            return patients_df
        except Exception:
            print("Файл с данными не удалось прочитать!")

    # Функция для начала работы класса (разбор полученных значений из json)
    def Start(self):
        offline = self.ParseJson()

        # Получения значения из JSON по названию ключа
        try:
            name = offline["Name"].values
            count = offline["Count"].values
            salary = offline["Salary"].values
            descrip = offline["Description"].values
        except Exception:
            print("Файл json не содержит указанный ключ!")
            return

        # Заполняем список обьектов, полученными данными
        for i in range(name.size):
            self.ListObject.append(Object(name[i], count[i], salary[i], descrip[i]))
            i += 1

        return self.ListObject
