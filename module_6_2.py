class Vehicle:
    __COLOR_VARIANTS = ['green', 'blue', 'white', 'red']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Марка машины: {self.__model}'
    def get_horsepower(self):
        return f'Мощность машины: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Цвет нельзя изменить на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5




car = Sedan('Roma', 'Nissan', 500, 'orange')
car.print_info()
car.set_color('black')
car.owner = 'Artem'
car.print_info()
