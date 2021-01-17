from slot_faker.providers import BaseProvider
import math
import random

class Provider(BaseProvider):
    def percentage(self, integer: bool = False):
        percent = self.random_int(1, 10000) / 100
        if integer:
            return f"{percent:.0f}%"
        if random.getrandbits(1):
            return f"{percent:.0f}%"
        return f"{percent:.01f}%"


    def percentage_less_than_25(self):
        percent = self.random_int(5, 25, 5)
        return f"{percent}%"