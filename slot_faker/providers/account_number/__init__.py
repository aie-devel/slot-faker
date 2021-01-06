from faker.providers import BaseProvider
import string

class Provider(BaseProvider):
    generic_formats = (
        '%#-####{{random_int}}{{random_letter}}#',
        '%######{{random_int}}??',
        '%#-?##{{random_int}}??',
        '??-{{random_int}}{{random_int}}'
    )

    bank_account_formats = (
        '##########',
        '###########',
        '############'
    )

    def account_number(self):
        pattern = self.random_element(self.generic_formats)
        return self.bothify(
            self.generator.parse(pattern),
            letters=string.ascii_uppercase
        )

    def routing_number(self):
        pattern = '##########'
        return self.numerify(pattern)

    def bank_account_number(self):
        pattern = self.random_element(self.bank_account_formats)
        return self.numerify(pattern)