from faker.providers import BaseProvider


class Provider(BaseProvider):

    def number(self, min: int = 0, max: int = 100):
        return self.random_int(min=min, max=max)