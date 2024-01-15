BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта 'Книга'

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц

        Пример:
        >>> book = Book(1, 'Название книги', 500)
         """
        if not isinstance(id_, int):
            raise TypeError(f'Параметр id_ должен иметь тип int')
        if id_ <= 0:
            raise ValueError(f'Параметр id_ должен быть положительным')
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError(f'Параметр name должен иметь тип str')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError(f'Параметр pages должен иметь тип int')
        if id_ <= 0:
            raise ValueError(f'Параметр pages должен быть положительным')
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        """
        Создание и подготовка к работе объекта 'Книга'

        :param books: Список книг

        Пример:
        >>> library = Library()
         """
        if books is None:
            books = []
        elif not isinstance(books, list):
            raise TypeError(f'Параметр books должен иметь тип list')
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Функция, возврящающая идентификатор для добавления новой книги

        Пример:
        >>> library = Library()
        >>> library.get_next_book_id()
        1
        """
        if not self.books:
            return 1
        else:
            return max(self.books, key=lambda book: book.id_).id_ + 1

    def get_index_by_book_id(self, id_: int) -> int:
        """
        Функция, возврящающая индекс книги по идентификатору

        Пример:
        >>> book = Book(1, 'Название книги', 500)
        >>> library = Library([book])
        >>> library.get_index_by_book_id(1)
        0
        """
        for ind, book in enumerate(self.books):
            if book.id_ == id_:
                return ind
        raise ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
