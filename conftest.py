import pytest
import allure
from api.api_client import ApiClient
from faker import Faker


fake = Faker()


@allure.title("Api client init")
@pytest.fixture()
def client():
    client = ApiClient()
    yield client


@pytest.fixture()
def temp_book(client):
    book_response = client.add_book(fake.pystr(), fake.name(), fake.pybool(), fake.pyint(min_value=0, max_value=3000))
    yield book_response.json['book']
    client.delete_book(book_response.json['book']['id'])

