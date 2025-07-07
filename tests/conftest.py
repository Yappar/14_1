import pytest

from src.products import Product
from src.category import Category


@pytest.fixture
def product():
    return Product("Мороженное", "Молочные изделия", 55.5, 10)


@pytest.fixture
def first_category():
    return Category(
        name="Кондитерские изделия",
        description="Сладости и выпечка",
        products=[
            Product("Мороженное", "Молочные изделия", 55.5, 10),
            Product("Молоко", "Молочные изделия", 70.0, 20),
            Product("Конфеты", "Кондитерские изделия", 140.0, 100),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Мясной отдел",
        description="мясо, колбасы",
        products=[
            Product("Фарш", "Полуфабрикаты", 1500.0, 50),
            Product("Сосиски", "Полуфабрикаты", 100.0, 70),
        ],
    )
