import pytest


def test_Product_LawnGrass_init(Product_LawnGrass1):
    assert Product_LawnGrass1.name == "Газонная трава"
    assert Product_LawnGrass1.description == "Элитная трава для газона"
    assert Product_LawnGrass1.price == 500.0
    assert Product_LawnGrass1.quantity == 20
    assert Product_LawnGrass1.country == "Россия"
    assert Product_LawnGrass1.germination_period == "7 дней"
    assert Product_LawnGrass1.color == "Зеленый"


def test_Product_LawnGrass_add(Product_LawnGrass1, Product_LawnGrass2):
    assert Product_LawnGrass1 + Product_LawnGrass2 == 16750


def test_Product_LawnGrass_add_error(Product_LawnGrass1):
    with pytest.raises(TypeError):
        result = Product_LawnGrass1 + 1
