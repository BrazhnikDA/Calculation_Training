class Object:
    Name: str           # Название
    Count: int          # Количество
    Salary: int         # Стоимость/Зарплата
    Description: str    # Описание

    # Конструктор
    def __init__(self, _Name, _Count, _Salary, _Desription):
        self.Name = _Name
        self.Count = _Count
        self.Salary = _Salary
        self.Description = _Desription

    # Относительно индекса (от 0 до 3) возвращаем нужное поле
    def __getitem__(self, key):
        if key == 0:
            return self.getName(self)
        if key == 1:
            return self.getCount(self)
        if key == 2:
            return self.getSalary(self)
        if key == 3:
            return self.getDescription(self)

    def __setitem__(self, key, value):
        if key == 0:
            return self.setName(value)
        if key == 1:
            return self.setCount(value)
        if key == 2:
            return self.setSalary(value)
        if key == 3:
            return self.setDescription(value)
            
    def getName(self):
        return self.Name

    def setName(self, _Name):
        self.Name = _Name

    def getCount(self):
        return self.Count

    def setCount(self, _Count):
        self.Count = _Count

    def getSalary(self):
        return self.Salary

    def setSalary(self, _Salary):
        self.Salary = _Salary

    def getDescription(self):
        return self.Description

    def setDescription(self, _Description):
        self.Description = _Description
