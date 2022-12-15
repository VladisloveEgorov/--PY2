import doctest


class University:
    def __init__(self, capacity_students: int, count_students: int, date_foundation: int):
        """
        Создание и подготовка к работе объекта "Университет"

        :param capacity_students: Общее число мест в университете
        :param count_students: Число занятых мест
        :param date_foundation: Дата основания университета

        Примеры:
        >>> university = University(15000, 12500, 1891)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_students, int):
            raise TypeError('Вместительность студентов должна быть int')
        if capacity_students < 0:
            raise ValueError('Вместительность студентов должна принимать положительное значение')
        if capacity_students < count_students:
            raise ValueError('Вместительность студентов не должна быть меньше числа студентов')
        self.capacity_students = capacity_students

        if not isinstance(date_foundation, int):
            raise TypeError
        self.date_foundation = date_foundation

        if not isinstance(count_students, int):
            raise TypeError
        if count_students < 0:
            raise ValueError
        self.count_students = count_students

    def add_students(self, add_st: int):

        """
        Зачисление (отчисление) студентов из университета.
        
        :param add_st: Кол-во зачисляемых(отчисляемых) студентов
        :raise TypeError: Если type(add_st) не int
        :raise ValueError: Если число обучающихся студентов выйдет за рамки общего
                           количества мест (0; capacity_students), то вызываем ошибку
                           
        Примеры:
        >>> university = University(15000, 12500, 1891)
        >>> university.add_students(1500)
        """
        if not isinstance(add_st, int):
            raise TypeError('Количество студентов должно быть типа int')
        ...

    def free_place(self) -> int:

        """
        Определение количества свободных мест
        :return: Количества свободных мест

        Примеры:
        >>> university = University(15000, 12500, 1891)
        >>> university.free_place()
        """
        ...


class Car:
    def __init__(self, motor: str, data_release: int):
        """
        Создание и подготовка к работе объекта "Авто"

        :param motor: Тип мотора
        :param data_release: Дата выпуска

        Примеры:
        >>> car = Car('ДВС', 2003)
        """

        if not isinstance(data_release, int):
            raise TypeError

        if data_release < 0:
            raise ValueError

        self.motor = motor
        self.data_release = data_release

    def is_motor(self, motor: str) -> bool:
        """
        Функция, которая проверяет - данный мотор стоит на авто или нет

        :param motor: Тип мотора
        :return: На авто стоит данный мотор

        Примеры:
        >>> car = Car('ДВС', 2003)
        >>> car.is_motor('ДВС')
        """
        ...

    def euro_standart(self) -> int:
        """
        Определение какому евростандарту соответсвует авто

        :return: Номер евростандарта

        Примеры:
        >>> car = Car('ДВС', 2003)
        >>> car.euro_standart()
        """
        ...


class Museum:
    def __init__(self, type_: str, number_exhibits: int):
        """
        Создание и подготовка к работе объекта "Музей"

        :param type_: Тип музея
        :param number_exhibits: Число экспонатов

        Примеры:
        >>> museum = Museum('historic', 75)
        """

        if not isinstance(number_exhibits, int):
            raise TypeError

        if number_exhibits < 0:
            raise ValueError

        self.type_ = type_
        self.number_exhibits = number_exhibits

    def museum_type_is(self, type_: str) -> bool:
        """
        Функция, которая проверяет - тип музея

        :param type_: Тип музея
        :return: Музей данного типа

        Примеры:
        >>> museum = Museum('historic', 75)
        >>> museum.museum_type_is('historic')
        """
        ...

    def scale_museum(self) -> str:
        """
        Функция определит масштаб музея(районный, городской, государственный) по количеству экспонатов

        :return: Масштаб музея

        Примеры:
        >>> museum = Museum('historic', 75)
        >>> museum.scale_museum()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
