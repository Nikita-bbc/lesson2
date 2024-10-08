class Horse:
    def __init__(self, *params):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__(*params)

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    def __init__(self, *params):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        super().__init__(*params)

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self, *params):
        super().__init__(*params)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
    def get_pos(self):
        _tuple = []
        _tuple.append(self.x_distance)
        _tuple.append(self.y_distance)
        return tuple(_tuple)
    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()