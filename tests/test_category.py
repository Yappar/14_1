def test_category_init(first_category, second_category):
    assert first_category.name == "Кондитерские изделия"
    assert first_category.description == "Сладости и выпечка"
    assert len(first_category.products) == 3
    assert len(second_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5
