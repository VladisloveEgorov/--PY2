import doctest


class University:
    def __init__(self, count_students: int, date_foundation: int):

        if not isinstance(date_foundation, int):
            raise TypeError

        self.date_foundation = date_foundation

        if not isinstance(count_students, int):
            raise TypeError

        if count_students < 0:
            raise ValueError

        self.count_students = count_students


class Car:
    def __init__(self, motor: str, data_release: int):

        if not isinstance(data_release, int):
            raise TypeError

        if data_release < 0:
            raise ValueError

        self.motor = motor
        self.data_release = data_release


class Museum:
    def __init__(self, type_: str, number_exhibits: int):

        if not isinstance(number_exhibits, int):
            raise TypeError

        if number_exhibits < 0:
            raise ValueError

        self.type_ = type_
        self.number_exhibits = number_exhibits


if __name__ == "__main__":
    doctest.testmod()
    pass
