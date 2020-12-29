from faker.providers import BaseProvider
import random

class Provider(BaseProvider):
    brands = {
        'iPhone': (
            '4', '5', '6', '7', '8', '9',
            'X', 'XS', 'XS Max', 'XR',
            '11', '11 Pro', '11 Pro Max',
            '12', '12 Pro', '12 Pro Max', '12 mini',
            'SE'
        ),
        'Samsung Galaxy': (
            'A21s', 'A31', 'A51', 'A71',
            'M31',
            'S10 Lite', 'S20', 'S20 Ultra',
            'Note10 Lite', 'Note20', 'Note20 Ultra'
        ),
        'OnePlus': ('8', '8 Pro'),
        'Google Pixel': ('4a', '5'),
        'Motorola One': ('', )
    }

    def phone(self):
        phone = self.random_element(self.brands.keys())
        if random.getrandbits(1):
            phone = f"{phone} {self.random_element(self.brands[phone])}"
        return phone

    def phone_brand(self):
        return self.random_element(self.brands.keys())

    def phone_version(self):
        phone = self.random_element(self.brands.keys())
        return f"{phone} {self.random_element(self.brands[phone])}"
