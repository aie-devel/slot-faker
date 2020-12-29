from faker import Faker
from slot_faker.config import PROVIDERS
from slot_faker.providers import phone

__version__ = '0.1.0'

class SlotFaker(Faker):
    def __init__(self):
        super().__init__(self, includes=PROVIDERS)
