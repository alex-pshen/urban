class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.current_floor = 1

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            step = (new_floor - self.current_floor) // abs(new_floor - self.current_floor)
            for i in range(self.current_floor, new_floor + step, step):
                print(i)
            self.current_floor = new_floor

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
print('')
h2.go_to(10)
print('')
h1.go_to(1)
print('')
h1.go_to(18)
print('')
h1.go_to(2)
print('')
h2.go_to(2)
print('')
h2.go_to(1)