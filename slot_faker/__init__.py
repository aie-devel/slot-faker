import csv
from functools import partial
from pathlib import Path

from faker import Faker

from slot_faker.config import PROVIDERS
from slot_faker.providers import phone

__version__ = '0.1.0'


class CustomValues:
    def __init__(self, **kwargs):
        self._add_methods(**kwargs)

    def _add_methods(self, **kwargs):
        for method_name, values_list in kwargs.items():
            object.__setattr__(
                self,
                method_name,
                tuple(values_list)
            )


class SlotFaker(Faker):
    def __init__(self):
        super().__init__(includes=PROVIDERS)

    def load_custom(self, csv_file: Path):
        custom_values = {}
        with open(csv_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                method_name, *values = row
                custom_values.setdefault(method_name, []).extend(values)
        _custom_values = getattr(self, '_custom_values', None)
        if not _custom_values:
            _custom_values = CustomValues()
            object.__setattr__(
                self,
                '_custom_values',
                _custom_values
            )
        _custom_values._add_methods(**custom_values)
        for method_name in custom_values:
            object.__setattr__(
                self,
                method_name,
                partial(self.random_element, getattr(self._custom_values, method_name))
            )

    def add_label(self, group, **kwargs):
        if not kwargs:
            return
        self.set_arguments(group, kwargs)
