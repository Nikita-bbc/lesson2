class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError()

        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration

        current_value = self.pointer
        self.pointer += self.step
        return current_value


obj = Iterator(-5, 1)
for value in obj:
    print(value, end=' ')
print()
try:
    obj1 = Iterator(5, 1, 0)
    for value in obj1:
        print(value, end=' ')
except StepValueError:
    print('Шаг не может быть равен 0')

obj3 = Iterator(16, 5, -2)
for value in obj3:
    print(value, end=' ')
print()