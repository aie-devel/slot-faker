from faker.providers import BaseProvider as FakerBaseProvider
from faker import Generator


class BaseProvider(FakerBaseProvider):
    def __init__(self):
        generator = Generator()
        super().__init__(generator)