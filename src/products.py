class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity  # количество
        self.full_price = price * quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб, Остаток: {self.quantity} шт."

    """" Название продукта, 80 руб. Остаток: 15 шт."""

    def __add__(self, other):
        return self.full_price + other.full_price

    @classmethod
    def new_product(cls, product):
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = (
            price
            if price > 0
            else print("Цена не должна быть нулевая или отрицательная")
        )


# if __name__ == "__main__":
#     product1 = Product("Мороженное", "Молочные изделия", 55.5, 10)
#     product2 = Product("Молоко", "Молочные изделия", 70.0, 20)
#     product3 = Product("Конфеты", "Кондитерские изделия", 140.0, 100)
#     product4 = Product("Фарш", "Полуфабрикаты", 1500.0, 50)
#     product5 = Product("Сосиски", "Полуфабрикаты", 100.0, 70)
#
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     product6 = Product.new_product("Жвачка", "Кондитер", 20.0, 40)
#     print(product6.name)
#     print(product6.description)
#     print(product6.price)
