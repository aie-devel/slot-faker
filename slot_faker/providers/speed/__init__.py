from slot_faker.providers import BaseProvider
import random
import inflect


class Provider(BaseProvider):
    plural = inflect.engine().plural

    distance = {
        'millimeter': 'mm',
        'centimeter': 'cm',
        'meter': 'm',
        'kilometer': 'km',
        'foot': 'f',
        'mile': 'm'
    }

    per = {
        'm': 'p',
        'f': 'p'
    }

    time_long = (
        'second',
        'minute',
        'hour'
    )

    time_short = (
        's',
        'm',
        'h'
    )

    def speed(self, unit: str = None, min: int = 0, max: int = 120):
        s = self.random_int(min, max)
        units = self.plural(unit, s) if unit else self._random_units(s)
        return f"{s} {units}"

    def _random_units(self, count: int):
        d = self.random_element(self.distance.keys())
        if random.getrandbits(1):
            t = self.random_element(self.time_long)
            return f"{self.plural(d, count)} per {t}"
        d = self.distance.get(d)
        p = self.per.get(d, '/')
        t = self.random_element(self.time_short)
        return f"{d}{p}{t}"