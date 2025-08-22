import pytest


def test_Product_Smartphone_init(Product_Smartphone1):
    assert Product_Smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert Product_Smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert Product_Smartphone1.price == 180000.0
    assert Product_Smartphone1.quantity == 5
    assert Product_Smartphone1.efficiency == 95.5
    assert Product_Smartphone1.model == "S23 Ultra"
    assert Product_Smartphone1.memory == 256
    assert Product_Smartphone1.color == "Серый"


def test_Product_Smartphone_add(Product_Smartphone1, Product_Smartphone2):
    assert Product_Smartphone1 + Product_Smartphone2 == 2580000


def test_Product_Smartphone_add_error(Product_Smartphone1, Product_Smartphone2):
    with pytest.raises(TypeError):
        result = Product_Smartphone1 + 1
