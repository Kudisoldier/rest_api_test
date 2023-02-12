from book import Book


def test_books_retrieval(client):
    books_response = client.get_books()
    assert books_response.status_code == 200
    for elem in books_response.json['books']:
        assert Book(**elem)


def test_book_retrieval(client, temp_book):
    book_response = client.get_book(temp_book['id'])
    assert book_response.status_code == 200
    assert Book(**book_response.json['book'])




