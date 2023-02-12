from book import Book
import utils


def test_books_retrieval(client):
    books_response = client.get_books()
    assert books_response.status_code == 200
    for elem in books_response.json['books']:
        assert Book(**elem)


def test_book_retrieval(client, temp_book):
    book_response = client.get_book(temp_book['id'])
    assert book_response.status_code == 200
    assert Book(**book_response.json['book'])


def test_book_add(client):
    random_book_data = utils.random_book()
    book_response = client.add_book(*random_book_data)
    book_json = book_response.json['book']
    assert book_response.status_code == 201
    assert Book(**book_json)
    assert (book_json['name'], book_json['author'],
            book_json['isElectronicBook'], book_json['year']) == random_book_data


def test_book_update(client, temp_book):
    random_book_data = utils.random_book()
    update_response = client.update_book_info(temp_book['id'], *random_book_data)
    book_json = update_response.json['book']
    book_obj = Book(**book_json)
    assert update_response.status_code == 200
    assert book_obj
    assert (book_json['name'], book_json['author'],
            book_json['isElectronicBook'], book_json['year']) == random_book_data

    book_response = client.get_book(temp_book['id'])
    assert Book(**book_response.json['book']) == book_obj


def test_book_delete(client, temp_book):
    delete_response = client.delete_book(temp_book['id'])

    assert delete_response.status_code == 200
    assert delete_response.json['result'] is True

    book_response = client.get_book(temp_book['id'])
    assert book_response.status_code == 404




