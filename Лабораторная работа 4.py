
if __name__ == "__main__":
    class Crane:
        """
        Базовый класс кран.
        """
        def __init__(self, name: str, lifting_capacity: (float, int), mobility: int):
            """ Инициализация экземпляра класса.
            :param name: Название крана
            :param lifting_capacity: Грузоподъемность
            :param mobility: Степень подвижности
            Пример: >>> crane = Crane(Portal, 35, 4)
            """
            self.name = name
            self.lifting_capacity = lifting_capacity
            self.mobility = mobility

        def __str__(self):
            """ Реализация магического метода __str__"""
            return f"Кран {self.name}. Грузоподъемность {self.lifting_capacity}. Степень подвижности {self.mobility}"

        def __repr__(self):
            """ Реализация магического метода __repr__"""
            return f"{self.__class__.__name__}(name = {self.name!r}, lifting_capacity = {self.lifting_capacity!r}," \
                   f" mobility = {self.mobility!r})"

        def up(self, metr: int) -> None:
            """
            подъем груза
            Примеры:
            >>> crane = Crane(Portal, 35, 4)
            >>> crane.up(40)
            """
            ...

        def down(self, metr: int) -> None:
            """ спуск груза """
            ...

        @property
        def name_(self) -> str:
            return self._name

        @name_.setter
        def name_(self, name: str) -> None:
            if not isinstance(name, str):
                raise TypeError("Название крана должно быть типа str")
            self.name = name

        @property
        def lifting_capacity_(self) -> (float, int):
            return self.lifting_capacity

        @lifting_capacity_.setter
        def lifting_capacity_(self, lifting_capacity: (float, int)) -> None:
            """Определяется грузоподъемность крана"""
            if not isinstance(lifting_capacity, (float, int)):
                raise TypeError("Грузоподъемность должна быть типа (float, int)")
            self.lifting_capacity = lifting_capacity

        @property
        def mobility_(self) -> int:
            return self.mobility

        @mobility_.setter
        def mobility_(self, mobility: int) -> None:
            """Определяется степень подвижности"""
            if not isinstance(mobility, int):
                raise TypeError("Степень подвижности должна быть типом int")
            if mobility <= 1:
                raise ValueError("Степень подвижности должна быть больше 1")
            self.mobility = mobility

    class GantryCrane(Crane):
        """Дочерний класс - Козловой кран
        :param shifting: Механизм перемещения
        """
        def __init__(self, name: str, lifting_capacity: (float, int), mobility: int, shifting: str):
            """Вызов конструктора базового класса"""
            super().__init__(name, lifting_capacity, mobility)
            self.shifting = shifting

        def __str__(self):
            return f"Кран {self.name}. Грузоподъемность {self.lifting_capacity}. Степень подвижности {self.mobility}," \
                   f" Механизм перемещения  {self.shifting}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name = {self.name!r}, lifting_capacity = {self.lifting_capacity!r}," \
                   f" mobility={self.mobility!r}, shifting = {self.shifting!r})"

        def up(self, metr: int) -> None:
            super().up(metr)

        def down(self, metr: int) -> None:
            """ спуск груза """
            ...

        @property
        def shifting_(self) -> str:
            return self.shifting

        @shifting_.setter
        def shifting_(self, shifting: str) -> None:
            """Определяется механизм перемещения крана"""
            if not isinstance(equipment, str):
                raise TypeError("Механизм перемещения должен быть типом str")
            self.shifting = shifting

    class TowerCrane(Crane):
        """Дочерний класс - Башенный кран
        :param height: Высота крана
        """
        def __init__(self, name: str, lifting_capacity: (float, int), mobility: int, height: int):
            """Вызов конструктора базового класса"""
            super().__init__(name, lifting_capacity, mobility)
            self.height = height

        def __str__(self):
            return f"Кран {self.name}. Грузоподъемность {self.lifting_capacity}. Степень подвижности {self.mobility}," \
                   f" Высота крана  {self.height}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name = {self.name!r}, lifting_capacity = {self.lifting_capacity!r}," \
                   f" mobility = {self.mobility!r}, height = {self.height!r})"

        def up(self, metr: int) -> None:
            """ подъем груза """
            ...

        def down(self, metr: int) -> None:
            super().down(metr)

        @property
        def height_(self) -> int:
            return self.height

        @height_.setter
        def height_(self, height: int):
            """Определяется высота крана"""
            if not isinstance(height, int):
                raise TypeError("Высота крана должна быть типом int")
            if height <= 15:
                raise ValueError("Высота крана должна быть больше 15")
            self.height = height
    pass
