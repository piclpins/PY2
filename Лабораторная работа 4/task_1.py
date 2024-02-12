from abc import ABC, abstractmethod
from typing import Union


class Rocket(ABC):
    NAME = None

    def __init__(self, mass, height, diameter):
        """
        Создание и подготовка к работе абстрактного объекта 'Ракета'.
        Создание экземпляров данного абстрактного класса не допускается.
        При попытке создать экземпляр класса, вызывается ошибка TypeError,
        поскольку класс является абстрактным.

        :param mass: Масса ракеты, кг
        :param height: Длина ракеты, м
        :param diameter: Диаметр ракеты, м
        """
        self.mass = mass
        self.height = height
        self.diameter = diameter

    @property
    def mass(self) -> int:
        return self._mass

    @mass.setter
    def mass(self, mass: int) -> None:
        if not isinstance(mass, int):
            raise TypeError
        if mass <= 0:
            raise ValueError
        self._mass = mass

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: Union[float, int]) -> None:
        if not isinstance(height, Union[float, int]):
            raise TypeError
        if height <= 0:
            raise ValueError
        self._height = height

    @property
    def diameter(self) -> float:
        return self._diameter

    @diameter.setter
    def diameter(self, diameter: Union[float, int]) -> None:
        if not isinstance(diameter, Union[float, int]):
            raise TypeError
        if diameter <= 0:
            raise ValueError
        self._diameter = diameter

    def calc_lengthening(self) -> Union[float, int]:
        """
        Функция, вычисляющая удлинение (отношение длины к диаметру) ракеты
        """
        return self.height / self.diameter

    @abstractmethod
    def calc_effectivity(self):
        """
        Абстрактный метод, вычисляющий эффективность ракеты.
        Критерией эффективности зависит от типа ракеты, поэтому метод обязательно
        должен быть перегружен в дочерних классах.
        """
        ...

    def __str__(self):
        return "Экземпляр абстрактного класса 'Ракета'"

    def __repr__(self):
        return f"{self.__class__.__name__}(mass={self.mass}, height={self.height}, diameter={self.diameter})"


class CarrierRocket(Rocket):
    NAME = 'Ракета-носитель'

    def __init__(self, mass, height, diameter, payload):
        """
        Создание и подготовка к работе объекта 'Ракета-носитель'.

        :param mass: Стартовая масса ракеты, кг
        :param height: Длина ракеты, м
        :param diameter: Диаметр ракеты, м
        :param payload: Масса полезной нагрузки, кг
        """
        super().__init__(mass, height, diameter)
        self.payload = payload

    @property
    def payload(self) -> int:
        return self._payload

    @payload.setter
    def payload(self, payload) -> None:
        if not isinstance(payload, Union[float, int]):
            raise TypeError
        if payload <= 0:
            raise ValueError
        self._payload = payload

    def calc_effectivity(self) -> Union[float, int]:
        """
        Метод, вычисляющий эффективность ракеты-носителя.
        В качестве критерия эффективности принято отношение
        массы полезной нагрузки к стартовой массе ракеты.
        """
        return self.payload / self.mass

    def __str__(self) -> str:
        return "Экземпляр класса 'Ракета-носитель'"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(mass={self.mass}, height={self.height}," \
               f" diameter={self.diameter}, payload={self.payload})"


class CombatMissile(Rocket):
    NAME = 'Боевая ракета'

    def __init__(self, mass, height, diameter, power):
        """
        Создание и подготовка к работе объекта 'Боевая ракета'.

        :param mass: Стартовая масса ракеты, кг
        :param height: Длина ракеты, м
        :param diameter: Диаметр ракеты, м
        :param power: Мощность ракеты, кт
        """
        super().__init__(mass, height, diameter)
        self.power = power

    @property
    def power(self) -> int:
        return self._power

    @power.setter
    def power(self, power) -> None:
        if not isinstance(power, Union[float, int]):
            raise TypeError
        if power <= 0:
            raise ValueError
        self._power = power

    def calc_effectivity(self) -> Union[float, int]:
        """
        Метод, вычисляющий эффективность боевой ракеты.
        В качестве критерия эффективности принято отношение
        мощности ракеты к ее стартовой массе.
        """
        return self.power / self.mass

    def __str__(self) -> str:
        return "Экземпляр класса 'Боевая ракета'"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(mass={self.mass}, height={self.height}," \
               f" diameter={self.diameter}, power={self.power})"


if __name__ == "__main__":
    pass
