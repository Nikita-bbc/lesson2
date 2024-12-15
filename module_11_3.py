import inspect


class Example:
    def __init__(self, numbers):
        self.numbers = numbers

    def square(self):
        for number in self.numbers:
            if isinstance(number, str) is False:
                print(f'Квадрат числа {number} = {number ** 2}')

    def square_root(self):
        for number in self.numbers:
            if isinstance(number, str) is False:
                if isinstance(number ** 0.5, int):
                    print(f'Корень числа {number} равен = {number ** 0.5}')
                else:
                    print(f'Корень числа {number} примерно равен = {round(number ** 0.5, 2)}')

    def word(self):
        for elem in self.numbers:
            if isinstance(elem, str):
                print(elem)


def introspection_info(obj):
    my_dict = dict()
    my_dict['Тип объекта'] = type(obj)
    my_dict['атрибуты объекта'] = dir(obj)
    my_dict['Методы объекта'] = inspect.getmembers(obj)
    return my_dict


list_digits = Example([4, 5, 6, 7, 9, 'tee'])
print(introspection_info(list_digits))
number_info = introspection_info((4, 5, 6))
print(number_info)
