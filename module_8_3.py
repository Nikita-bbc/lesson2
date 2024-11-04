class Car:
    def __init__(self, model, __vin, numbers):
        self.model = model
        self.vin_number = __vin
        self.numbers = numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(numbers)
    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) is False:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number < 10 ** 6 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True
    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) is False:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 111111111, 'т001тр')
except IncorrectCarNumbers as exc:
    print(exc.message)
except IncorrectVinNumber as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
