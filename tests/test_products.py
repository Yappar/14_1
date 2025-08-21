def test_product_init(product):
    assert product.name == "Мороженное"
    assert product.description == "Молочные изделия"
    assert product.price == 55
    assert product.quantity == 10

    assert str(product) == "Мороженное, 55 руб, Остаток: 10 шт."

    product.price = -100
    assert product.price is None

    product.price = 0
    assert product.price is None

    product8 = product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert product8.name == "Samsung Galaxy S23 Ultra"


def test_product_price_sum(product, product2):
    result = product + product2
    assert result == 950
