import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_successfully_set_genre_for_book(self):
        collector = BooksCollector()
        test_name = 'Тестовое имя'
        genre = 'Фантастика'
        collector.add_new_book(test_name)
        collector.set_book_genre(test_name, genre)
        assert collector.get_book_genre(test_name) == genre

    @pytest.mark.parametrize(
        'test_name, genre',
        [
            ('Тестовое имя', 'Детективы'),
            ('Тестовое имя 2', 'Ужасы')
        ]
    )
    def test_get_book_genre_successfully_get_book_genre_by_name(self, test_name, genre):
        collector = BooksCollector()
        collector.add_new_book(test_name)
        collector.set_book_genre(test_name, genre)
        assert collector.get_book_genre(test_name) == genre

    @pytest.mark.parametrize(
        'test_name, genre',
        [
            ('Тестовое имя', 'Детективы'),
            ('Тестовое имя 2', 'Ужасы')
        ]
    )
    def test_get_books_with_specific_genre_successfully_get_list_of_books_with_specific_genre(self, test_name, genre):
        collector = BooksCollector()
        collector.add_new_book(test_name)
        collector.set_book_genre(test_name, genre)
        assert test_name in collector.get_books_with_specific_genre(genre)

    @pytest.mark.parametrize(
        'test_name, genre',
        [
            ('Тестовое имя', 'Детективы'),
            ('Тестовое имя 2', 'Ужасы')
        ]
    )
    def test_get_books_genre_successfully_get_books_genre_by_name(self, test_name, genre):
        collector = BooksCollector()
        collector.add_new_book(test_name)
        collector.set_book_genre(test_name, genre)
        books_genre = collector.get_books_genre()
        assert test_name in books_genre
        assert books_genre[test_name] == genre

    @pytest.mark.parametrize(
        'test_name, genre',
        [
            ('Тестовое имя', 'Фантастика'),
            ('Тестовое имя 2', 'Мультфильмы'),
            ('Тестовое имя 3', 'Комедии')
        ]
    )
    def test_get_books_for_children_successfully_get_list_of_books_for_children(self, test_name, genre):
        collector = BooksCollector()
        collector.add_new_book(test_name)
        collector.set_book_genre(test_name, genre)
        books_for_children = collector.get_books_for_children()
        assert test_name in books_for_children

    def test_add_book_in_favorites_successfully_added_to_favorites(self):
        collector = BooksCollector()
        test_name = 'test_name'
        collector.add_new_book(test_name)
        collector.add_book_in_favorites(test_name)
        assert test_name in collector.favorites

    def test_delete_book_from_favorites_successfully_deleted_from_favorites(self):
        collector = BooksCollector()
        test_name = 'test_name'
        collector.add_new_book(test_name)
        collector.add_book_in_favorites(test_name)
        collector.delete_book_from_favorites(test_name)
        assert test_name not in collector.favorites

    def test_get_list_of_favorites_books_successfully_get_list_of_favorites_books(self):
        collector = BooksCollector()
        test_name = 'test_name'
        collector.add_new_book(test_name)
        collector.add_book_in_favorites(test_name)
        assert test_name in collector.get_list_of_favorites_books() and collector.get_list_of_favorites_books() == list
        collector.delete_book_from_favorites(test_name)
        assert test_name not in collector.get_list_of_favorites_books() and collector.get_list_of_favorites_books() == list
