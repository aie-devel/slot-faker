import csv
from functools import partial
from pathlib import Path

from faker import Faker

from slot_faker.config import PROVIDERS
from slot_faker.providers import phone

__version__ = '0.1.0'


class CustomValues:
    def __init__(self, **kwargs):
        for method_name, values_list in kwargs.items():
            object.__setattr__(
                self,
                method_name,
                tuple(values_list)
            )


class SlotFaker(Faker):
    def __init__(self, **custom_values):
        super().__init__(includes=PROVIDERS)
        if custom_values:
            self._custom_values = CustomValues(**custom_values)
            for method_name in custom_values:
                object.__setattr__(
                    self,
                    method_name,
                    partial(self.random_element, getattr(self._custom_values, method_name))
                )

    @classmethod
    def load_custom_values(cls, csv_file: Path):
        custom_values = {}
        with open(csv_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                method_name, *values = row
                custom_values.setdefault(method_name, []).extend(values)
        return cls(**custom_values)
