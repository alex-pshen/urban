from threading import Thread
from random import randint
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number) -> None:
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def run(self) -> None:
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables) -> None:
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            try:
                table = next(filter(lambda t: t.guest == None, self.tables))
                table.guest = guest
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
                guest.start()
            except StopIteration:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        working = True
        while working:
            working = False
            for t in self.tables:
                if t.guest != None:
                    if t.guest.is_alive():
                        working = True
                    else:
                        print(f"{t.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {t.number} свободен")
                        t.guest = None
                if t.guest == None and not self.queue.empty():
                    working = True
                    t.guest = self.queue.get()
                    print(
                        f"{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}"
                    )
                    t.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    "Maria",
    "Oleg",
    "Vakhtang",
    "Sergey",
    "Darya",
    "Arman",
    "Vitoria",
    "Nikita",
    "Galina",
    "Pavel",
    "Ilya",
    "Alexandra",
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
