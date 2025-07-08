from optparse import Option

from src.products import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name:str, description:str, products:Option[list[Product]]=None):
        self.name = name
        self.description = description
        self.products = products if products else [] # products or []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


if __name__ == "__main__":

    category1 = Category(
        "Кондитерские изделия",
        "Сладости и выпечка",
        ["Конфеты", "Булочки", "Выпечка"]
    )
    category2 = Category(
        "Мясной отдел", "мясо, колбасы", ["Фарш", "Колбаса", "Мясо", "Сосиски"]
    )
    print(Category.category_count)
    print(category2.product_count)
    print(Category.product_count)
