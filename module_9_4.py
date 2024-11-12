from random import choice

first = 'Мама мыла раму'
second = 'Рамена было мало'
result = list(map(lambda x, y: x == y, first, second))
print(result)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for i in data_set:
                f.write(f'{i}\n')
    return write_everything


write = get_advanced_writer('data.txt')
write('Это строка', ['А', 'Это', 'уже', 'число', '5', 'в', 'списке'])


class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return choice(self.words)


res = MysticBall(['Hi', 'Hello', 'Hey'])
print(res())
