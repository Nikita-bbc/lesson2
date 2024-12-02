import random
import threading
import time
from queue import Queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue(len(tables))
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guest(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(-а)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                if not self.queue.empty() and not table.guest:
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f'{next_guest.name} вышел(-а) из очереди и сел(-а) за стол номер {table.number}')


names = ['Artem', 'Egor', 'Kirill', 'Ivan', 'Olga']
guests = [Guest(name) for name in names]
tables = [Table(number) for number in range(1, 4)]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guest()


