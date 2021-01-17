from slot_faker.providers import BaseProvider
import inflect
import random


class Provider(BaseProvider):
    plural = inflect.engine().plural

    units_long = (
        'gram',
        'kilogram',
        'pound',
        'ton',
        'ounce'
    )

    units_short = (
        'g',
        'kg',
        'lb.',
        'ton',
        'oz.'
    )

    def weight(self, unit: str = None, min: int = 0, max: int = 200):
        w = self.random_int(min, max)
        units = self.plural(unit, w) if unit else self._random_units(w)
        return f"{w} {units}"

    def _random_units(self, count: int):
        if random.getrandbits(1):
            return self.random_element(self.units_short)
        return self.plural(
            self.random_element(self.units_long),
            count
        )

