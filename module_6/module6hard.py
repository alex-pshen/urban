import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides) -> None:
        if not self.__is_valid_sides(*sides):
            raise ValueError(
                f"""Стороны фигуры должны быть целыми положительными числами.
                                 количество сторон - {Figure.sides_count}.
                             """
            )
        if not self.__is_valid_color(*color):
            raise ValueError(
                f"Цвет фигуры задаётся в формате (R, G, B) тремя целыми числами от 0 до 255 включительно."
            )
        self.__sides = sides
        self.__color = color
        self.filled = True

    def get_color(self):
        return list(self.__color)

    @staticmethod
    def __is_valid_color(r, g, b) -> bool:
        return (
            type(r) == type(g) == type(b) == int
            and 0 <= r < 256
            and 0 <= g < 256
            and 0 <= b < 256
        )

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    @classmethod
    def __is_valid_sides(cls, *sides):
        return len(sides) == cls.sides_count and [
            type(l) in (int, float) and (l > 0 and int(l) == l) for l in sides
        ]

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(list(self.get_sides()))

    def set_sides(self, *sides):
        if len(sides) == self.sides_count:
            self.__sides = sides


class Circle(Figure):

    def __init__(self, color, *sides) -> None:
        Circle.sides_count = 1
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / 2 / math.pi

    def get_square(self):
        return math.pi * (self.__radius**2)


class Triangle(Figure):
    def __init__(self, color, *sides) -> None:
        Triangle.sides_count = 3
        super().__init__(color, *sides)

    @classmethod
    def _Figure__is_valid_sides(cls, *sides):
        if len(sides) == 3:
            a, b, c = sides
            if a > b + c and b > a + c and c > a + b:
                return Figure.__is_valid_sides(sides)
            else:
                raise ValueError(
                    f"""Треугольников со сторонами {a}, {b}, {c} существовать не может"""
                )
        return False

    def get_square(self):
        p = len(self) / 2
        a, b, c = self.get_sides()
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return S


class Cube(Figure):
    def __init__(self, color, side) -> None:
        Cube.sides_count = 12
        super().__init__(color, *((side,) * 12))

    def get_volume(self):
        return self.get_sides()[0] ** 3


# MAIN
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
