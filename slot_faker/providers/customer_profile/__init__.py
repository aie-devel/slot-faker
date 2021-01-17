from slot_faker.providers import BaseProvider
import random

class Provider(BaseProvider):

    def email_user_name(self, first_name: str, last_name: str):
        p = 100 * random.random()
        if p < 50:
            first_name, last_name = last_name, first_name
        if p > 75:
            last_name = last_name[0]
        if p < 25:
            first_name = first_name[0]
        if random.getrandbits(1):
            return f"{first_name}.{last_name}"
        return f"{first_name}{last_name}"

    def customer_profile(self):
        first_name =  self.generator.first_name()
        last_name = self.generator.last_name()
        email_user_name = self.email_user_name(first_name, last_name)
        email_domain = self.generator.free_email_domain()
        email_address = f"{email_user_name}@{email_domain}"
        birthdate = self.generator.date_of_birth()

        return {
            'first_name': first_name,
            'last_name': last_name,
            'email_address': email_address,
            'ssn': self.generator.ssn(),
            'account_number': self.generator.account_number(),
            'birthdate': birthdate,
            'postal_address': self.generator.postal_address(),
            'user_name': f"{email_user_name}{birthdate.year}",
            'password': self.generator.password(special_chars=False)
        }