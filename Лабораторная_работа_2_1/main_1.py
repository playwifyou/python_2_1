

class Furniture:
    """
    Абстрактный класс для описания предметов мебели.
    """

    def __init__(self, material: str, weight: float):
        """
        Конструктор для инициализации атрибутов материала и веса.
        Material: Материал изготовления мебели.
        Weight: Вес мебели в килограммах.

        Пример >> table = Furniture(material="wood", weight=20.0)
        """
        if weight <= 0:
            raise ValueError("Вес мебели должен быть положительным значением")
        self.material = material
        self.weight = weight

    def move(self, new_location: str) -> None:
        """
        Переместить мебель в указанное место.
        New_location: Строка, указывающая новое место.
        """
        pass

    def get_info(self) -> str:
        """
        Получить информацию о предмете мебели.
        Return: Строка с описанием мебели.
        """
        pass


class Tree:
    """
    Абстрактный класс для описания дерева как биологического объекта.
    """

    def __init__(self, age: int, height: float):
        """
        Конструктор для инициализации возраста и высоты дерева.
        Age: Возраст дерева в годах.
        Height: Высота дерева в метрах.
        """
        if age < 0 or height <= 0:
            raise ValueError("Возраст и высота должны быть положительными значениями")
        self.age = age
        self.height = height

    def grow(self, years: int) -> None:
        """
        Увеличить возраст и высоту дерева за несколько лет.
        Years: Количество лет роста.
        Пример: >>> tree.grow(5)
        """
        pass

    def photosynthesize(self) -> None:
        """
        Запустить процесс фотосинтеза.
        """
        pass


class Stack:
    """
    Абстрактный класс для описания структуры данных стек.
    """

    def __init__(self, max_size: int):
        """
        Конструктор для инициализации максимального размера стека.
        Max_size: Максимальное количество элементов в стеке.
        """
        if max_size <= 0:
            raise ValueError("Максимальный размер стека должен быть положительным числом")
        self.max_size = max_size
        self.elements = []

    def push(self, item: int) -> None:
        """
        Добавить элемент в стек.
        Item: Элемент для добавления.
        """
        pass

    def is_empty(self) -> bool:
        """
        Проверить, пуст ли стек.
        Return: True, если стек пуст, иначе False.
        Пример: >>> stack1.is_empty()
        """
        pass
