class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    product1 = Product("Мороженное", "Молочные изделия", 55.5, 10)
    product2 = Product("Молоко", "Молочные изделия", 70.0, 20)
    product3 = Product("Конфеты", "Кондитерские изделия", 140.0, 100)
    product4 = Product("Фарш", "Полуфабрикаты", 1500.0, 50)
    product5 = Product("Сосиски", "Полуфабрикаты", 100.0, 70)

    print(product1.name)
    print(product1.description)
    print(product1.price)
