import doctest


class Fan:
    def __init__(self, max_power: int, color: str):
        """
        Создание и подготовка к работе класса 'Вентилятор'

        :param max_power: Максимальная мощность вентилятора
        :param color: Цвет вентилятора

        :raise TypeError: Вызываем ошибку, если введенное значение принадлежит не тому типу данных
        :raise ValueError: Вызываем ошибку, если  максимальная мощность вентилятора неположительное число

        Пример:
        >>> fan1 = Fan(100, 'black')
        """
        if not isinstance(max_power, int):
            raise TypeError('Максимальная мощность должна иметь тип int')
        if not max_power > 0:
            raise ValueError('Максимальная мощность вентилятора должна быть положительной')
        self.max_power = max_power

        if not isinstance(color, str):
            raise TypeError('Цвет должен иметь тип str')
        self.color = color

        self.power = max_power

        self.is_on = False

    def change_power(self, power: int):
        """
        Функция, изменяющая мощность вентилятора

        :param power: Мощность вентилятора
        :raise TypeError: Вызываем ошибку, если мощность не типа int
        :raise ValueError: Вызывем ошибку, если мощность больше максимальной или неположительное число

        Пример:
        >>> fan1 = Fan(100, 'black')
        >>> print(fan1.power)
        100
        >>> fan1.change_power(60)
        >>> print(fan1.power)
        60
        """
        if not isinstance(power, int):
            raise TypeError('Мношность должна иметь тип int')
        if not 0 < power <= self.max_power:
            raise ValueError('Мощность должна быть меньше максимальной и больше нуля')
        self.power = power

    def switch(self):
        """
        Функция, включающая и выключащая вентилятор

        Пример:
        >>> fan1 = Fan(100, 'black')
        >>> print(fan1.is_on)
        False
        >>> fan1.switch()
        >>> print(fan1.is_on)
        True
        """
        self.is_on = not self.is_on


if __name__ == "__main__":
    doctest.testmod()
