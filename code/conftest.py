import pytest
import allure
from api.api_client import ApiClient
import utils


@allure.title("Api client init")
@pytest.fixture()
def client():
    client = ApiClient()
    yield client


@pytest.fixture()
def temp_book(client):
    book_response = client.add_book(*utils.random_book())
    yield book_response.json['book']
    client.delete_book(book_response.json['book']['id'])
