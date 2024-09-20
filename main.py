class House:
    def __init__(self, name: str, number_of_floors: int):
        """Инициализатор класса"""
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        """Метод класса"""
        if 1 <= new_floor <= self.number_of_floors:
            for n in range(new_floor):
                print(n + 1)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        """Позволяет применять функцию len() к экземплярам класса"""
        return self.number_of_floors

    def __str__(self):
        """Применяется для отображения информации об объекте класса для пользователей,
        например для функций print, str."""
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        """Метод возвращает True, если два сравниваемых объекта равны между собой"""
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        """Метод возвращает True, если первый объекта меньше второго объекта"""
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        """Метод возвращает True, если первый объекта меньше либо равен второму объекту"""
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        """Метод возвращает True, если первый объекта больше второго объекта"""
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        """Метод возвращает True, если первый объекта больше либо равен второму объекту"""
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        """Метод возвращает True, если первый объекта не равен второму объекту"""
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        """Метод увеличивает количество этажей на величину 'value',
        если 'value' принадлежит классу 'int'"""
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        """Метод увеличивает количество этажей на величину 'value',
                если 'value' принадлежит классу 'int'"""
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        """Метод увеличивает количество этажей на величину 'value',
                если 'value' принадлежит классу 'int'"""
        if isinstance(value, int):
            self.number_of_floors += value
            return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
