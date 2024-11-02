count = 0


def personal_sum(numbers):
    global count
    count = 0
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
            count += 1
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        for j in range(len(numbers)):
            try:
                return personal_sum(numbers)[0] / count
            except ZeroDivisionError:
                return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average('1, 2, 3')}')
print(f'Результат 2: {calculate_average([1, 'String', 3, 'String else'])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
