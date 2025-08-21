import pytest

from src.products import Product
from src.category import Category
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass


@pytest.fixture
def product():
    return Product("Мороженное", "Молочные изделия", 55, 10)


@pytest.fixture
def product2():
    return Product("Сникерс", "Кондитерские изделия", 80, 5)


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


@pytest.fixture
def Product_Smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def Product_Smartphone2():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def Product_LawnGrass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def Product_LawnGrass2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
