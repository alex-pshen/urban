class IncorrectVinNumber(Exception):
    def __init__(self, message) -> None:
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message) -> None:
        self.message = message


class Car:
    @staticmethod
    def __is_valid_vin(vin_number):
        if type(vin_number) != int:
            raise IncorrectVinNumber("Некорректный тип vin номера")
        elif not (1_000_000 <= vin_number <= 9_999_999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            return True

    @staticmethod
    def __is_valid_numbers(numbers):
        if type(numbers) != str:
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        elif len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        else:
            return True

    def __init__(self, model, vin, numbers) -> None:
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers


try:
    first = Car("Model1", 1000000, "f123dj")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{first.model} успешно создан")

try:
    second = Car("Model2", 300, "т001тр")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{second.model} успешно создан")

try:
    third = Car("Model3", 2020202, "нет номера")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{third.model} успешно создан")
