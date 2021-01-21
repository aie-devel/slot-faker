import csv
from functools import partial
from pathlib import Path

from faker import Faker, Factory
from typing import List, Tuple, Union


from slot_faker.config import PROVIDERS
from slot_faker.providers import phone

__version__ = '0.1.0'

class CustomSlotType:
    def __init__(self, name: str, values: List[Union[str, int]]):
        self.name = name
        self.values = [
            str(value).strip()
            for value in values
            if value
        ]

    def get_slot_values(self, custom_slot_values: List[Union[str, int]]):
        return [
            slot_value
            for item in custom_slot_values
            if (
                    (slot_value := str(item).strip())
                    and slot_value in self.values
            )
        ]


class CustomSlotMethod:
    def __init__(self, name: str, slot_type: str, values: Union[List, Tuple]):
        self.name = name
        self.type = slot_type
        self.values = tuple(values)
        self.generator = Factory.create()

    def __call__(self):
        return self.generator.random_element(self.values)

    def set_type(self, slot_type: CustomSlotType):
        self.type = slot_type
        self.values = self.type.get_slot_values(self.values)



class CustomValues:
    def __init__(self, types: Path, methods: Path, slotterances: Path = None):
        self.types = {
            slot_type: CustomSlotType(
                name=slot_type,
                values=values
            )
            for slot_type, values in self.read_csv(types)
        }
        self.methods = {
            slot_method: CustomSlotMethod(
                name=slot_method,
                slot_type='elements_list',
                values=values
            )
            for slot_method, values in self.read_csv(methods)
        }
        if slotterances:
            for slot_method, values in self.read_csv(slotterances):
                self.methods.update(
                    {
                        slot_method: CustomSlotMethod(
                            name=slot_method,
                            slot_type='slotterance',
                            values=values
                        )
                    }
                )

    def read_csv(self, csv_file: Path):
        with open(csv_file, 'r') as f:
            for row in csv.reader(f):
                yield row[0], [cell.strip() for cell in row[1:]]

    def get_method(self, method: str, _type: str = None):
        if (slot_method := self.methods.get(method, None)):
            if (slot_type := self.types.get(_type, None)):
                slot_method.set_type(slot_type)
            return slot_method

    def get_type(self, slot_type: str):
        return self.types.get(slot_type, None)





class SlotFaker(Faker):
    def __init__(self, domain: str = None, custom: Path = None, custom_dict: dict = None):
        super().__init__(includes=PROVIDERS)
        self.domain = domain
        self._custom_values = CustomValues()
        if custom:
            self.load_custom_values(custom, custom_dict=custom_dict)

    def load_custom(self, csv_file: Path, custom_dict: dict = None):
        custom_values = {**custom_dict} or {}
        with open(csv_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                method_name, *values = row
                if method_name not in custom_values:
                    custom_values.setdefault(method_name, {}).update(
                        {
                            'type': 'elements_list',
                            'values': []
                        }
                    )
                custom_values[method_name].setdefault('values', []).extend(values)
        self._custom_values._add_methods(custom_values)
        for method_name, method in self._custom_values._get_methods().items():
            object.__setattr__(
                self,
                method_name,
                method
            )

    def export_custom(self):
        out_file = Path(__file__).absolute().parent / f"{self.domain}_custom_values.csv"


    def add_label(self, group, **kwargs):
        if not kwargs:
            return
        self.set_arguments(group, kwargs)
