# Lambda-функция
first = "Мама мыла раму"
second = "Рамена мало было"

list_ = list(map(lambda a, b: a == b, first, second))
print(list_)


# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "a") as file:
            for item in data_set:
                file.write(str(item) + "\n")

    return write_everything


write = get_advanced_writer("example.txt")
write("Это строчка", ["А", "это", "уже", "число", 5, "в", "списке"], {1: "a", 2: "b"})


# Метод __call__
from random import choice


class MysticBall:
    def __init__(self, *args) -> None:
        self.words = args

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall("Да", "Нет", "Наверное")
print(first_ball())
print(first_ball())
print(first_ball())
