from api.base_api import BaseApi


class ApiClient(BaseApi):
    def __init__(self):
        super().__init__()
        self.base_url = 'http://127.0.0.1:5000/'

    def add(self):
        response = self.request('get', 'api/books')
        return response


