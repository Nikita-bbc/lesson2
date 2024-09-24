class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        args = args[0]
        cls.houses_history.append(args)
        return object.__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors
    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.floors:
                print(f'Номер этажа {i}')
            else:
                print('Такого этажа не существует')
                break
    def __del__(self):
        print(f'{self.name} был снесён, но он останется в истории')
    def __len__(self):
        return self.floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'
    def __add__(self, value):
        if isinstance(value, int):
            self.floors = self.floors + value
        elif isinstance(value, House):
            self.floors = self.floors + value.floors
        return self
    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        elif isinstance(other, House):
            return self.floors == other
    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        elif isinstance(other, int):
            return self.floors < other
    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        elif isinstance(other, int):
            return self.floors > other
    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        elif isinstance(other, int):
            return self.floors <= other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        elif isinstance(other, int):
            return self.floors >= other
    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        elif isinstance(other, int):
            return self.floors != other
    def __iadd__(self, value):
        return self.__add__(value)
    def __radd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)


del h2
del h3

print(House.houses_history)
