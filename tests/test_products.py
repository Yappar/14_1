def test_product_init(product):
    assert product.name == "Мороженное"
    assert product.description == "Молочные изделия"
    assert product.price == 55.5
    assert product.quantity == 10
