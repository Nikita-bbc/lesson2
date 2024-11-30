import threading
import time
import random


class Bank:
    lock = threading.Lock()

    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        for _ in range(100):
            random_digit_pl = random.randint(50, 500)
            self.balance += random_digit_pl
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {random_digit_pl}, текущий баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            random_digit_mn = random.randint(50, 500)
            print(f'Запрос на {random_digit_mn}')
            if random_digit_mn <= self.balance:
                self.balance -= random_digit_mn
                print(f'Снятие: {random_digit_mn}, текущий баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


first_time = Bank(500)

thread_1 = threading.Thread(target=Bank.deposit, args=(first_time, ))

thread_2 = threading.Thread(target=Bank.take, args=(first_time, ))

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print(first_time.balance)