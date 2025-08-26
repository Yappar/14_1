from src.products import Product


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


def test_middle_quantity(first_category, category_without_product):
    assert first_category.middle_price() == 88.5
    assert category_without_product.middle_price() == 0


def test_customs_exception(capsys, first_category):
    # assert first_category.product_count == 3

    product_add = Product("Мороженное", "Молочные изделия", 55.5, 0)
    first_category.add_product(product_add)
    message = capsys.readouterr()
    assert (
        message.out.strip().split("\n")[-2]
        == "Нельзя задать задачу с нулевым количеством"
    )
    assert (
        message.out.strip().split("\n")[-1] == "Обработка добавления задачи завершена"
    )

    product_add = Product("Мороженное", "Молочные изделия", 55.5, 10)
    first_category.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Задача добавлена успешно"
    assert (
        message.out.strip().split("\n")[-1] == "Обработка добавления задачи завершена"
    )
