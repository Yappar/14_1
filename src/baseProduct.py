from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс, определяющий интерфейс для классов продуктов."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """
        Абстрактный метод класса для создания нового экземпляра продукта.

        Args:
            *args: Произвольные позиционные аргументы для создания продукта.
            **kwargs: Произвольные именованные аргументы для создания продукта.
        """
        pass
