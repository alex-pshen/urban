import threading as th
import time


class Knight(th.Thread):
    __INITIAL_ENEMYS = 100

    def __init__(self, name, power) -> None:
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = Knight.__INITIAL_ENEMYS
        ndays = 0
        while enemies > 0:
            time.sleep(1)
            ndays += 1
            enemies -= self.power
            print(
                f"{self.name} сражается {ndays} дней, осталось {max(enemies, 0)} воинов."
            )
        print(f"{self.name} одержал победу спустя {ndays} дней(дня)!")


# Создание класса
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")
