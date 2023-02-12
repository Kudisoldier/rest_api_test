from api.base_api import BaseApi


class ApiClient(BaseApi):
    def __init__(self):
        super().__init__()
        self.base_url = 'http://127.0.0.1:5000/'

    def get_books(self):
        response = self.request('get', 'api/books')
        return response

    def get_book(self, book_id):
        response = self.request('get', f'api/books/{book_id}')
        return response

    def add_book(self, name, author=None, isElectronicBook=None, year=None):
        data = {"name": name}

        if isElectronicBook is not None:
            data["isElectronicBook"] = isElectronicBook
        if author is not None:
            data["author"] = author
        if year is not None:
            data["year"] = year

        response = self.request('post', 'api/books', json=data)
        return response

    def update_book_info(self, book_id, name, author, isElectronicBook, year):
        data = {
            "author": author,
            "isElectronicBook": isElectronicBook,
            "name": name,
            "year": year
        }
        response = self.request('put', f'api/books/{book_id}', json=data)
        return response

    def delete_book(self, book_id):
        response = self.request('delete', f'api/books/{book_id}')
        return response
