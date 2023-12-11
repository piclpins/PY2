import doctest
from typing import Union


class LightBulb:
    def __init__(self, socle: str, power: int, light_flow: int):
        """
        Создание и подготовка к работе объекта 'Лампочка'

        :param socle: Тип цоколя (Е14, Е27, Е40) символ Е - в русской раскладке
        :param power: Мощность
        :param light_flow: Световой поток

        Пример:
        >>> bulb = LightBulb('Е14', 50, 400)
        """
        if not isinstance(socle, str):
            raise TypeError(f'Параметр socle должен иметь тип str')
        if socle not in ['Е14', 'Е27', 'Е40']:
            raise ValueError('Параметр socle должен принимать одно из следующих значений: Е14, Е27, Е40 (русская раскладка)')
        self.socle = socle

        self.check_value(power)
        self.power = power

        self.check_value(light_flow)
        self.light_flow = light_flow

    def check_value(self, value: int):
        """
        Функция, проверяющая корректность введенных данных

        :param value: Переданное значение атрибута

        :raise TypeError: Вызываем ошибку, если введено значение неверного типа
        :raise TypeError: Вызываем ошибку, если введено неположительное число
        """
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть типа int')
        if not value > 0:
            raise ValueError(f'Значение {value} должно быть положительным')

    def is_right_socle(self, our_socle: str):
        """
        Функция, проверяющая, подходит ли лампочка под наш цоколь

        :param our_socle: Тип нашего цоколя (Е14, Е27, Е40)
        :return: True - подходит, False - нет

        Пример:
        >>> bulb = LightBulb('Е27', 60, 600)
        >>> bulb.is_right_socle('Е27')
        True
        """
        return self.socle == our_socle

    def calculate_energy_use(self, hours: Union[int, float]):
        """
        Функция, вычисляющая электропотребление лампочки за определенное время

        :param hours: Время, в течение которого работает лампочка (в часах)

        :return: электропотребление лампочки за время hours

        :raise TypeError: Вызываем ошибку, если введено значение неверного типа
        :raise TypeError: Вызываем ошибку, если введено неположительное число

        Пример:
        >>> bulb = LightBulb('Е27', 60, 600)
        >>> time = 13
        >>> bulb.calculate_energy_use(time)
        780
        """
        if not isinstance(hours, (int, float)):
            raise TypeError('Параметр hours принимает int или float')
        if not hours > 0:
            raise ValueError('Параметр hours принимает положительное число')
        return self.power * hours


if __name__ == "__main__":
    doctest.testmod()
