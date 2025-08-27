from src.products import Product
from src.exceptions import ZeroQuantityProduct


class Category:
    products: list
    category_count = 0  # Общее количество категорий
    product_count = 0  # Общее количество уникальных товаров, счетчик продуктов

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = (
            products if products else []
        )  # products or [] # Приватный атрибут списка товаров
        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов:{sum(product.quantity for product in self.__products)} шт."

    def add_product(self, product: Product):
        """Добавляет товар в приватный список продуктов категории."""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct(
                        "Нельзя задать задачу с нулевым количеством"
                    )
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1  # Увеличиваем счетчик товаров
                print("Задача добавлена успешно")
            finally:
                print("Обработка добавления задачи завершена")
        else:
            raise TypeError

    """геттер который возвращает значения"""
    """ Декоратор property позволяет нам обращаться к методу как к атрибуту класса """

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)} \n"
        return products_str

    def middle_price(self):
        try:
            return sum(product.price for product in self.__products) / len(
                self.__products
            )
        except ZeroDivisionError:
            return 0

    """ используем метод add+product или сеттер"""

    # @products.setter
    # def products(self, product:Product):
    #     """Добавляет товар в приватный список продуктов категории."""
    #     self.__products.append(product)
    #     Category.product_count += 1 # Увеличиваем счетчик товаров


if __name__ == "__main__":
    product1 = Product("Мороженное", "Молочные изделия", 55.5, 10)
    product2 = Product("Молоко", "Молочные изделия", 70.0, 20)
    product3 = Product("Конфеты", "Кондитерские изделия", 140.0, 100)
    product4 = Product("Фарш", "Полуфабрикаты", 1500.0, 50)
    product5 = Product("Сосиски", "Полуфабрикаты", 100.0, 5)

    category1 = Category(
        "Кондитерские изделия", "Сладости и выпечка", [product1, product2, product3]
    )
    category2 = Category("Мясной отдел", "мясо, колбасы", [product4, product5])
    print(Category.category_count)
    print(category2.products)
    print(Category.product_count)

    product6 = Product("Сосиска", "Полуфабрикаты", 100.0, 550)
    # category2.products = product6 # при использовании сеттера
    category2.add_product(product6)
    print(category2.products)
