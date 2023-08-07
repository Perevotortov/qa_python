import pytest


class TestBooksCollector:

    def test_add_new_book_add_one_book(self, books_collector, books_collector_with_book):
        books_collector.add_new_book('Сказки')
        assert len(books_collector.get_books_genre()) == 2

    '''
    В этом тесте использую две фикстуры, первая создает экземпляр класса BooksCollector, вторая список с одной книгой
    проверка идет со значением длины списка =2, потому что мы добавили в конец списка книгу Сказки, и список стал:
    [{Сияние:Ужасы}, {Сказки:''}]. 2 элемента списка, длина == 2.
    '''

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_set_genre_for_one_book(self, books_collector):
        books_collector.add_new_book('Сияние')
        books_collector.set_book_genre('Сияние', 'Ужасы')
        assert books_collector.get_book_genre('Сияние') == 'Ужасы'

    '''
    В этом тесте не использую фикстуру со списком, чтобы проверить что новой книге без жанра задается жанр
    '''

    def test_get_book_genre_get_genre_from_book(self, books_collector, books_collector_with_book):
        assert books_collector.get_book_genre('Сияние') == 'Ужасы'

    '''
    Использование фикстуры позволило сократить тест до одной строки. Иначе пришлось бы создавать книгу, ей задавать жанр
    .
    В ситуации, когда предыдущие две функции не работают - этот тест бы тоже не заработал. Это базированный тест.
    '''

    def test_get_books_with_specific_genre_get_one_book_with_genre(self, books_collector, books_collector_with_book):
        assert books_collector.get_books_with_specific_genre('Ужасы') == ['Сияние']

    '''
    Тест на то, что в списке из фикстуры по жанру Ужасы только одна книга 
    '''

    def test_get_books_genre_get_list_of_books(self, books_collector, books_collector_with_book):
        assert books_collector.get_books_genre() == {'Сияние': 'Ужасы'}

    '''
        Тест на то, что в список из фикстуры соответствует выводу get_books_genre
    '''

    @pytest.mark.parametrize('books', [{"Сияние": "Ужасы", "Сказки": "Мультфильмы"}])
    def test_get_books_for_children_get_books_for_kids(self, books_collector, books):
        for book_name, book_genre in books.items():
            books_collector.add_new_book(book_name)
            books_collector.set_book_genre(book_name, book_genre)
        assert books_collector.get_books_for_children() == ['Сказки']

    '''
    Проверяем что добавленная в список книга Сказки является выводом get_books_for_children.
    Дополнительно можно добавить вторую фикстуру в тест, и при запуске будет также проверяться что книга "Сияние" 
    не попала в список, но это будет тест, затрагивающий две проверки (наличие в списке, отсутствие) так что я не стал
    ее прописывать, лучше такой тест сделать отдельно.

    UPD: Добавил параметризацию, две книги. Создал цикл который добавляет две книги в список книг, затем проверяю что
    при вызове списка кнги для детей, книга Ужасы не попадет в выборку. 
    '''

    def test_add_book_in_favorites_add_book_to_favorites(self, books_collector, books_collector_with_book):
        books_collector.add_book_in_favorites('Сияние')
        assert 'Сияние' in books_collector.get_list_of_favorites_books()

    '''
    Проверка что книга из фикстуры добавлена в фавориты, альтернативный код: books_collector.favorites == ['Сияние']
    После этого теста буду использовать другую фикстуру, в которой уже выполнено действия добавления в избранное из 
    этого теста
    '''

    def test_delete_book_from_favorites_delete_from_favorites(self, books_collector, books_collector_with_favorite):
        books_collector.delete_book_from_favorites('Сияние')
        assert 'Сияние' not in books_collector.get_list_of_favorites_books()

    '''
    Проверка что Сияние удалено из фаворитов, добавление Сияния в фавориты произошло при обращении к фикстуре
    '''

    def test_get_list_of_favorites_books_get_list_of_favorites(self, books_collector, books_collector_with_favorite):
        assert books_collector.get_list_of_favorites_books() == ['Сияние']

    '''
    Проверка, что полученный список избранного содержит книгу из фикстуры
    '''


'''Тестовый класс для проверки фикстур
class TestFixtures:
    #Проверка что фикстура добавила книгу в список
    def test_books_collector_with_book(self, books_collector_with_book, books_collector):
        assert books_collector.get_books_genre() == {'Сияние': 'Ужасы'}

    #Проверка что Сияние добавлено в избранное
    def test_books_collector_with_favorite(self, books_collector, books_collector_with_favorite):
        assert 'Сияние' in books_collector.favorites
'''