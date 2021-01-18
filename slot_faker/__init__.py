import csv
from functools import partial
from pathlib import Path

from faker import Faker, Factory
from typing import List, Tuple, Union


from slot_faker.config import PROVIDERS
from slot_faker.providers import phone

__version__ = '0.1.0'


class CustomSlotMethod:
    def __init__(self, name: str, values: Union[List, Tuple]):
        self.name = name
        self.values = tuple(values)
        self.generator = Factory.create()

    def __call__(self):
        return self.generator.random_element(self.values)



class CustomValues:
    def __init__(self, **kwargs):
        self._methods = []
        self._add_methods(**kwargs)


    def _add_methods(self, **kwargs):
        for method_name, values_list in kwargs.items():
            method = CustomSlotMethod(name=method_name, values=values_list)
            self._methods.append(method.name)
            object.__setattr__(
                self,
                method_name,
                method
            )

    def _get_methods(self):
        return {
            method_name: getattr(self, method_name)
            for method_name in self._methods
        }


class SlotFaker(Faker):
    def __init__(self, custom: Path = None):
        super().__init__(includes=PROVIDERS)
        self._custom_values = CustomValues()
        if custom:
            self.load_custom(custom)

    def load_custom(self, csv_file: Path):
        custom_values = {}
        with open(csv_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                method_name, *values = row
                custom_values.setdefault(method_name, []).extend(values)
        self._custom_values._add_methods(**custom_values)
        for method_name, method in self._custom_values._get_methods():
            object.__setattr__(
                self,
                method_name,
                method
            )

    def add_label(self, group, **kwargs):
        if not kwargs:
            return
        self.set_arguments(group, kwargs)
