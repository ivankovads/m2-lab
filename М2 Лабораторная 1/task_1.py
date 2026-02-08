# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
import doctest


class Book:

    """Класс, описывающий книгу как физический объект."""
    def __init__(self, title: str, page_count: int, is_hardcover: bool):
        """
        Создание и подготовка к работе объекта «Книга».

        :param title: Название книги
        :param page_count: Количество страниц
        :param is_hardcover: Признак твёрдого переплёта (True/False)

        Примеры:
        >>> book = Book("Война и мир", 1200, True)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(page_count, int):
            raise TypeError("Количество страниц должно быть типа int")
        if page_count <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.page_count = page_count

        if not isinstance(is_hardcover, bool):
            raise TypeError("Признак твёрдого переплёта должен быть типа bool")
        self.is_hardcover = is_hardcover

    def open(self, page: int) -> None:
        """
        Открывает книгу на указанной странице.

        :param page: Номер страницы для открытия
        :raises ValueError: Если номер страницы выходит за пределы книги

        Примеры:
        >>> book = Book("Мастер и Маргарита", 400, False)
        >>> book.open(150)
        >>> book.open(500)
        Traceback (most recent call last):
            ...
        ValueError: Номер страницы превышает общее количество страниц
        """
        if not isinstance(page, int):
            raise TypeError("Номер страницы должен быть типа int")
        if page < 1 or page > self.page_count:
            raise ValueError("Номер страницы превышает общее количество страниц")

    def bookmark(self, page: int) -> None:
        """
        Ставит закладку на указанную страницу.

        :param page: Номер страницы для закладки
        :raises ValueError: Если страница вне допустимого диапазона

        Примеры:
        >>> book = Book("Преступление и наказание", 600, True)
        >>> book.bookmark(300)
        """
        if not isinstance(page, int):
            raise TypeError("Номер страницы должен быть типа int")
        if page < 1 or page > self.page_count:
            raise ValueError("Страница для закладки вне допустимого диапазона")

    def get_info(self) -> str:
        """
        Возвращает краткую информацию о книге.

        :return: Строка с названием, количеством страниц и типом переплёта

        Примеры:
        >>> book = Book("Гарри Поттер", 350, False)
        >>> book.get_info()
        'Гарри Поттер, 350 стр., мягкий переплёт'
        """
        cover_type = "твёрдый переплёт" if self.is_hardcover else "мягкий переплёт"
        return f"{self.title}, {self.page_count} стр., {cover_type}"


class Printer:
    """Класс, описывающий принтер как офисное устройство."""

    def __init__(self, model: str, max_dpi: int, paper_capacity: int):
        """
        Создание и подготовка к работе объекта «Принтер».

        :param model: Модель принтера
        :param max_dpi: Максимальное разрешение печати (точек на дюйм)
        :param paper_capacity: Вместимость лотка для бумаги (листов)

        Примеры:
        >>> printer = Printer("HP LaserJet", 1200, 250)
        """
        if not isinstance(model, str):
            raise TypeError("Модель принтера должна быть типа str")
        if not model:
            raise ValueError("Модель принтера не может быть пустой")
        self.model = model

        if not isinstance(max_dpi, int):
            raise TypeError("Разрешение печати должно быть типа int")
        if max_dpi <= 0:
            raise ValueError("Разрешение печати должно быть положительным числом")
        self.max_dpi = max_dpi

        if not isinstance(paper_capacity, int):
            raise TypeError("Вместимость лотка должна быть типа int")
        if paper_capacity <= 0:
            raise ValueError("Вместимость лотка должна быть положительным числом")
        self.paper_capacity = paper_capacity
        self.current_paper = 0  # Текущее количество бумаги в лотке

    def load_paper(self, sheets: int) -> None:
        """
        Загружает бумагу в лоток принтера.

        :param sheets: Количество листов для загрузки
        :raises TypeError: Если sheets не число
        :raises ValueError: Если sheets отрицательное или превышает вместимость лотка

        Примеры:
        >>> printer = Printer("Canon PIXMA", 4800, 100)
        >>> printer.load_paper(50)
        >>> printer.current_paper
        50
        """
        if not isinstance(sheets, int):
            raise TypeError("Количество листов должно быть типа int")
        if sheets < 0:
            raise ValueError("Количество листов не может быть отрицательным")
        if self.current_paper + sheets > self.paper_capacity:
            raise ValueError("Превышена вместимость лотка для бумаги")
        self.current_paper += sheets

    def print_document(self, pages: int, dpi: int) -> None:
        """
        Печатает документ с заданным количеством страниц и разрешением.

        :param pages: Количество страниц для печати
        :param dpi: Разрешение печати (точек на дюйм)
        :raises ValueError: Если страниц больше, чем бумаги, или dpi превышает max_dpi

        Примеры:
        >>> printer = Printer("Epson L3150", 5760, 150)
        >>> printer.load_paper(100)
        >>> printer.print_document(20, 600)
        >>> printer.current_paper
        80
        """
        if not isinstance(pages, int) or not isinstance(dpi, int):
            raise TypeError("Параметры печати должны быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        if dpi > self.max_dpi:
            raise ValueError(f"Разрешение печати не может превышать {self.max_dpi} dpi")
        if pages > self.current_paper:
            raise ValueError("Недостаточно бумаги для печати")
        self.current_paper -= pages

    def get_status(self) -> str:
        """
        Возвращает текущий статус принтера.

        :return: Строка со статусом (модель, бумага, макс. разрешение)

        Примеры:
        >>> printer = Printer("Brother DCP", 2400, 200)
        >>> printer.load_paper(150)
        >>> printer.get_status()
        'Принтер Brother DCP: 150/200 листов, макс. 2400 dpi'
        """
        return (f"Принтер {self.model}: {self.current_paper}/{self.paper_capacity} листов, "
                f"макс. {self.max_dpi} dpi")


class Flashlight:
    """Класс, описывающий фонарик как портативное осветительное устройство."""

    def __init__(self, battery_capacity: int, brightness: int, is_waterproof: bool):
        """
        Создание и подготовка к работе объекта «Фонарик».

        :param battery_capacity: Ёмкость батареи (в мАч)
        :param brightness: Яркость света (в люменах)
        :param is_waterproof: Признак водонепроницаемости (True/False)

        Примеры:
        >>> flashlight = Flashlight(2000, 300, True)
        """
        if not isinstance(battery_capacity, int):
            raise TypeError("Ёмкость батареи должна быть типа int")
        if battery_capacity <= 0:
            raise ValueError("Ёмкость батареи должна быть положительной")
        self.battery_capacity = battery_capacity

        if not isinstance(brightness, int):
            raise TypeError("Яркость должна быть типа int")
        if brightness <= 0:
            raise ValueError("Яркость должна быть положительной")
        self.brightness = brightness

        if not isinstance(is_waterproof, bool):
            raise TypeError("Признак водонепроницаемости должен быть типа bool")
        self.is_waterproof = is_waterproof
        self.is_on = False  # Состояние фонарика: включён (True) или выключен (False)

        if __name__ == "__main__":
            doctest.testmod()  # тестирование примеров, которые находятся в документации
