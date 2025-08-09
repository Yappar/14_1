def test_product_init(product):
    assert product.name == "Мороженное"
    assert product.description == "Молочные изделия"
    assert product.price == 55.5
    assert product.quantity == 10

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
