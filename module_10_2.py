import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        counter = 100
        days = 0
        while counter >= 0:
            time.sleep(1)
            if counter - self.power < 0:
                days += 1
                break
            days += 1
            counter -= self.power
            print(f'{self.name}, сражается {days} дней(дня)(день), осталось {counter} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)')


thread_1 = Knight('Nikita', 15)
thread_2 = Knight('Alex', 30)

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print('Все битвы окончены!')




