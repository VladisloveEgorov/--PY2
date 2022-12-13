import doctest


class University:
    def __init__(self, capacity_students: int, count_students: int, date_foundation: int):

        if not isinstance(capacity_students, int):
            raise TypeError('Вместительность студентов должна быть int')

        if capacity_students < 0:
            raise ValueError('Вместительность студентов должна принимать положительное значение')

        if capacity_students < count_students:
            raise ValueError('Вместительность студентов не должна быть меньше числа студентов')

        if not isinstance(date_foundation, int):
            raise TypeError

        if not isinstance(count_students, int):
            raise TypeError

        if count_students < 0:
            raise ValueError

        self.capacity_students = capacity_studentss
        self.count_students = count_students
        self.date_foundation = date_foundation

    def add_students(self, add_st: int):
        # Функция, которая зачисляет/отчисляет студентов
        ...

    def free_place(self) -> int:
        # Функция определяет число свободных мест
        # return: Число свободных мест
        ...

    # Пример university = University(15000, 12500, 1891)
    #        university.free_place() -> 2500


class Car:
    def __init__(self, motor: str, data_release: int):

        if not isinstance(data_release, int):
            raise TypeError

        if data_release < 0:
            raise ValueError

        self.motor = motor
        self.data_release = data_release

    def is_motor(self, motor: str) -> bool:
        # Функция, которая проверяет данный мотор стоит на авто или нет
        # return: Является ли мотор таковым
        ...

    def euro_standart(self) -> int:
        # Функция определяет какому евростандарту соовтетствует авто по году выпуска
        # return: Евростандарт
        ...

    # Пример car = Car('ДВС', 2003)
    #        car.euro_standart() -> 3


class Museum:
    def __init__(self, type_: str, number_exhibits: int):

        if not isinstance(number_exhibits, int):
            raise TypeError

        if number_exhibits < 0:
            raise ValueError

        self.type_ = type_
        self.number_exhibits = number_exhibits

    def museum_type_is(self, type_: str) -> bool:
        # Функция, которая проверяет музей данного типа или нет
        # return: Является ли музей type_
        ...

    def scale_museum(self,) -> str:
        # Функция определит масштаб музея(районный, городской, государственный) по количеству экспонатов
        # return: Масштаб(str)
        ...

    # Пример museum = Museum('historic', 75)
    #        mesuem.museum_type_is('historic') -> True


if __name__ == "__main__":
    doctest.testmod()
    pass
