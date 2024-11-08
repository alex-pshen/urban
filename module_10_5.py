from multiprocessing import Pool
from time import time


class stopwatch:
    def __enter__(self) -> None:
        self.start = time()

    def __exit__(self, *_) -> None:
        print(f"Время выполнения кода {(time() - self.start):.2f} секунд")


def read_info(name):
    with open(name, "r") as file:
        all_data = [line for line in file]
        # return all_data   # Это копирование сильно замедляет многопроцессную версию


if __name__ == "__main__":
    file_names = [f"./file {number}.txt" for number in range(1, 5)]

    print("Линейный. ", end="")
    with stopwatch():
        for name in file_names:
            read_info(name)

    print("Многопроцессный. ", end="")
    with stopwatch():
        pool = Pool(processes=len(file_names))
        pool.map(read_info, file_names)
