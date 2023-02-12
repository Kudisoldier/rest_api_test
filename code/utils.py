from faker import Faker


fake = Faker()


def random_book():
    return fake.pystr(), fake.name(), fake.pybool(), fake.pyint(min_value=0, max_value=3000)
