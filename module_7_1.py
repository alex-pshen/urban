class Product:
    def __init__(self, name, weight, category) -> None:
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        with open(self.__file_name, "a+") as file:
            file.seek(0)
            return file.read()

    def add(self, *products):
        content = self.get_products()
        with open(self.__file_name, "a") as file:
            for p in products:
                if str(p) not in content:
                    file.write(str(p) + "\n")
                else:
                    print(f"Продукт {p} уже есть в магазине")


s1 = Shop()
p1 = Product("Potato", 50.5, "Vegetables")
p2 = Product("Spaghetti", 3.4, "Groceries")
p3 = Product("Potato", 5.5, "Vegetables")

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
