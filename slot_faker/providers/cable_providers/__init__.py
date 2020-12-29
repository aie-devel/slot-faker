from faker.providers import BaseProvider


class Provider(BaseProvider):
    companies = (
        'AT&T Wireless',
        'Verizon Wireless'
        'Spectrum',
        'CenturyLink',
        'EarthLink',
        'Viasat',
        'WOW!',
        'Frontier',
        'HughesNet',
        'Google Fiber',
        'Xfinity',
        'T-Mobile Wireless',
        'Dish'
    )

    def cable_internet_provider(self):
        return self.random_element(self.companies)

    def cable_provider(self):
        return self.cable_internet_provider()

    def internet_provider(self):
        return self.cable_internet_provider()