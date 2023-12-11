import doctest


class Account:
    def __init__(self, friends_list: list[str], nickname: str, age: int):
        """
        Создание и подготовка к работе класса 'Аккаунт'

        :param friends_list: Список друзей
        :param nickname: Имя пользователя
        :param age: Возраст пользователя

        :raise TypeError: Вызываем ошибку, если введенное значение принадлежит не тому типу данных
        :raise ValueError: Вызываем ошибку, если возраст - неположительное число

        Пример:
        >>> account1 = Account(['Настя', 'Володя', 'Ваня'], 'Ибрагим', 20)
        """
        if not isinstance(friends_list, list):
            raise TypeError('Список друзей должен иметь тип list')
        self.friends_list = friends_list

        if not isinstance(nickname, str):
            raise TypeError('Имя пользователя должно иметь тип str')
        self.nickname = nickname

        if not isinstance(age, int):
            raise TypeError('Возраст должен иметь тип int')
        if not age > 0:
            raise ValueError('Возраст должен быть положительным')
        self.age = age

        self.is_online = True

    def add_friend(self, nickname: str):
        """
        Функция, добавляющая нового друга по имени пользователя

        :param nickname: Имя пользователя

        :raise TypeError: Вызываем ошибку, если имя пользователя не типа str

        Пример:
        >>> account1 = Account(['Настя', 'Володя', 'Ваня'], 'Ибрагим', 20)
        >>> account1.add_friend('Богдан')
        >>> print(account1.friends_list)
        ['Настя', 'Володя', 'Ваня', 'Богдан']
        """
        if not isinstance(nickname, str):
            raise TypeError('Имя пользователя должно иметь тип str')
        self.friends_list.append(nickname)

    def change_status(self):
        """
        Функция, меняющая статус пользователя

        Пример:
        >>> account1 = Account(['Настя', 'Володя', 'Ваня'], 'Ибрагим', 20)
        >>> print(account1.is_online)
        True
        >>> account1.change_status()
        >>> print(account1.is_online)
        False
        """
        self.is_online = not self.is_online


if __name__ == "__main__":
    doctest.testmod()
