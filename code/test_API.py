from book import Book
import utils
import pytest
import allure


@allure.title("Позитивный тест получения списка книг")
@pytest.mark.positive
def test_books_retrieval(client):
    """Проверяем, что можно получить список книг и они соответствуют модели данных"""
    books_response = client.get_books()
    assert books_response.status_code == 200
    for elem in books_response.json['books']:
        assert Book(**elem)


@allure.title("Позитивный тест получения информации о книге")
@pytest.mark.positive
def test_book_retrieval(client, temp_book):
    """Проверяем, что можно получить корректную информацию о книге по ее айди"""
    book_response = client.get_book(temp_book['id'])
    assert book_response.status_code == 200
    assert Book(**book_response.json['book'])


@allure.title("Позитивный тест добавления книги")
@pytest.mark.positive
def test_book_add(client):
    """Проверяем, что можно создать книгу"""
    random_book_data = utils.random_book()
    book_response = client.add_book(*random_book_data)
    book_json = book_response.json['book']
    assert book_response.status_code == 201
    assert Book(**book_json)
    assert (book_json['name'], book_json['author'],
            book_json['isElectronicBook'], book_json['year']) == random_book_data


@allure.title("Позитивный тест изменения данных о книге")
@pytest.mark.positive
def test_book_update(client, temp_book):
    """Проверяем, что можно обновить информацию по айди"""
    with allure.step("Update info"):
        random_book_data = utils.random_book()
        update_response = client.update_book_info(temp_book['id'], *random_book_data)
        book_json = update_response.json['book']
        book_obj = Book(**book_json)
        assert update_response.status_code == 200
        assert book_obj
        assert (book_json['name'], book_json['author'],
                book_json['isElectronicBook'], book_json['year']) == random_book_data

    with allure.step("Check that data changed with get_book method"):
        book_response = client.get_book(temp_book['id'])
        assert Book(**book_response.json['book']) == book_obj


@allure.title("Позитивный тест удаления книги")
@pytest.mark.positive
def test_book_delete(client, temp_book):
    """Проверяем, что можно удалить книгу"""
    with allure.step("Delete existing book"):
        delete_response = client.delete_book(temp_book['id'])

        assert delete_response.status_code == 200
        assert delete_response.json['result'] is True

    with allure.step("Delete nonexistent book"):
        book_response = client.get_book(temp_book['id'])
        assert book_response.status_code == 404
        assert book_response.json['error'] == f'Book with id {temp_book["id"]} not found'


@pytest.mark.negative
def test_create_existing(client, temp_book):
    """Проверяем, что можно создать уже существующую книгу"""
    book_response = client.add_book(temp_book['name'], temp_book['author'],
                                    temp_book['isElectronicBook'], temp_book['year'])
    assert book_response.status_code == 201
    assert Book(**book_response.json['book'])


@pytest.mark.negative
def test_delete_nonexistent_book(client):
    """Проверяем, что нельзя удалить несуществующую книгу"""
    book_response = client.delete_book(0)
    assert book_response.status_code == 404
    assert book_response.json['error'] == 'Book with id 0 not found'


@pytest.mark.negative
@pytest.mark.parametrize("book_data", [(2, 'asd'), (2, 2, 2, "asd"), ('asd', False, 2, "asd")])
def test_create_with_invalid_data(client, book_data):
    """Проверяем, что нельзя создать книгу с некорректными данными, нарушиющих типы"""
    book_response = client.add_book(*book_data)
    assert book_response.status_code == 400
    assert book_response.json['error']
