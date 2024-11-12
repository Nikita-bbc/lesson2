first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(x[0]) - len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1]))
print(list(first_result))
try:
    second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
    print(list(second_result))
except IndexError:
    print('Не хватает элементов во втором списке')