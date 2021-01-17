from slot_faker.providers import BaseProvider


class Provider(BaseProvider):

    def number(self, min: int = 0, max: int = 100):
        return self.random_int(min=min, max=max)

    def count(self, singular: str, plural: str, min: int = 1, max: int = 10):
        count = self.random_int(min=min, max=max)
        if count == 1:
            return f"{count} {singular}"
        return f"{count} {plural}"
