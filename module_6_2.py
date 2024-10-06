class Vehicle:
    __color_variants = ['green', 'blue', 'white', 'red']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color

    def get_model(self):
        return f'Марка машины: {self.model}'
    def get_horsepower(self):
        return f'Мощность машины: {self.engine_power}'
    def get_color(self):
        return f'Цвет: {self.color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in self.__color_variants:
            self.color = new_color
        else:
            print('Цвет нельзя изменить')


class Sedan(Vehicle):
    __passengers_limit = 5




car = Sedan('Roma', 'Nissan', 500, 'orange')
car.print_info()
car.set_color('White')
car.set_color('BLacK')
car.owner = 'Artem'
car.print_info()