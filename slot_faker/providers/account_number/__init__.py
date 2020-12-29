from faker.providers import BaseProvider
import string

class Provider(BaseProvider):
    formats = (
        '%#-####{{random_int}}{{random_letter}}#',
        '%######{{random_int}}??',
        '%#-?##{{random_int}}??',
        '??-{{random_int}}{{random_int}}'
    )
    def account_number(self):
        pattern = self.random_element(self.formats)
        return self.bothify(
            self.generator.parse(pattern),
            letters=string.ascii_uppercase
        )