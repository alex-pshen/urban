from threading import Thread
from threading import Lock
from time import sleep
from random import randint


class Bank:
    def __init__(self) -> None:
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            a = randint(50, 500)
            self.balance += a
            print(f"Пополнение: {a}. Баланс: {self.balance}")
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for _ in range(100):
            a = randint(50, 500)
            print(f"Запрос на {a}")
            if self.balance >= a:
                self.balance -= a
                print(f"Снятие: {a}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bank = Bank()
th1 = Thread(target=Bank.deposit, args=(bank,))
th2 = Thread(target=Bank.take, args=(bank,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f"Итоговый баланс: {bank.balance}")
