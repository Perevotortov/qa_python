import pytest
from main import BooksCollector

@pytest.fixture() #scope=function по умолчанию
def books_collector():
    return BooksCollector()
#фикстура для класса BooksCollector, чтобы не создавать в каждом тесте отдельный класс

@pytest.fixture()
#scope=function по умолчанию, перед каждым тестом которому я ее передам, будет создаваться список [Сияние:Ужасы]
def books_collector_with_book(books_collector):
    books_collector.add_new_book("Сияние")
    books_collector.set_book_genre("Сияние", "Ужасы")
    return books_collector

@pytest.fixture()
#фикстура, которая добавляет сияние из фикстуры books_collector_with_book в список избранного
def books_collector_with_favorite(books_collector, books_collector_with_book):
    books_collector.add_book_in_favorites('Сияние')
    return books_collector

class TestFixtures:
    #Проверка что фикстура добавила книгу в список
    def test_books_collector_with_book(self, books_collector_with_book, books_collector):
        assert books_collector.get_books_genre() == {'Сияние': 'Ужасы'}

    #Проверка что Сияние добавлено в избранное
    def test_books_collector_with_favorite(self, books_collector, books_collector_with_favorite):
        assert 'Сияние' in books_collector.favorites