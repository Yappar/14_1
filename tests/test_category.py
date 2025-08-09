def test_category_init(first_category, second_category):
    assert first_category.name == "Кондитерские изделия"
    assert first_category.description == "Сладости и выпечка"
    assert len(first_category.products) == 112
    assert len(second_category.products) == 72

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_product_property(first_category):
    assert first_category.products == (
        "Мороженное, 55.5 руб, Остаток: 10 шт. \n"
        "Молоко, 70.0 руб, Остаток: 20 шт. \n"
        "Конфеты, 140.0 руб, Остаток: 100 шт. \n"
    )
