class House:
    __GROUND_FLOOR = 1

    def __init__(self, name, number_of_floors) -> None:
        if type(name) == str and type(number_of_floors) == int:
            self.name = name
            self.number_of_floors = number_of_floors
            self.current_floor = House.__GROUND_FLOOR
        else:
            raise TypeError("Правильно создавать объект House(str, int)")

    def go_to(self, new_floor) -> None:
        if new_floor < House.__GROUND_FLOOR or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            step = (new_floor - self.current_floor) // abs(
                new_floor - self.current_floor
            )
            for i in range(self.current_floor, new_floor + step, step):
                print(i)
            self.current_floor = new_floor

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return self.number_of_floors < other

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return (not self.__eq__(other)) and (not self.__lt__(other))

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        else:
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
