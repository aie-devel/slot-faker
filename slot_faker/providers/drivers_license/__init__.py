from faker.providers import BaseProvider
import string


class Provider(BaseProvider):

    states = {
        'Alabama': ('#{1,8}',),
        'Alaska': ('#{1,7}',),
        'Arizona': ('\\?#{8}', '#{9}'),
        'Arkansas': ('#{4,9}',),
        'California': ('\\?#{7}',),
        'Colorado': ('#{9}', '\\?#{3,6}', '\\?{2}#{2,5}'),
        'Connecticut': ('#{9};',),
        'Delaware': ('#{1,7}',),
        'District of Columbia': ('#{7}', '#{9}'),
        'Florida': ('\\?#{12}',),
        'Georgia': ('#{7,9}',),
        'Hawaii': ('\\?#{8}', '#{9}'),
        'Idaho': ('\\?{2}#{6}\\?', '#{9}'),
        'Illinois': ('\\?#{11}', '\\?#{12}'),
        'Indiana': ('\\?#{9}', '#{9}', '#{10}'),
        'Iowa': ('#{9}', '#{3}\\?{2}#{4}'),
        'Kansas': ('\\?#\\?#\\?', '\\?#{8}', '#{9}'),
        'Kentucky': ('\\?#{8}', '\\?#{9}', '#{9}'),
        'Louisiana': ('#{1,9}',),
        'Maine': ('#{7}', '#{7}\\?', '#{8}'),
        'Maryland': ('\\?#{12}',),
        'Massachusetts': ('\\?#{8}', '#{9}'),
        'Michigan': ('\\?#{10}', '\\?#{12}'),
        'Minnesota': ('\\?#{12}',),
        'Mississippi': ('#{9}',),
        'Missouri': ('\\?#{5,9}', '\\?#{6}R', '#{8}\\?{2}', '#{9}\\?', '#{9}'),
        'Montana': ('\\?#{8}', '#{13}', '#{9}', '#{14}'),
        'Nebraska': ('\\?#{6,8}',),
        'Nevada': ('#{9}', '#{10}', '#{12}', 'X#{8}'),
        'New Hampshire': ('#{2}\\?{3}#{5}',),
        'New Jersey': ('\\?#{14}',),
        'New Mexico': ('#{8}', '#{9}'),
        'New York': ('\\?#{7}', '\\?#{18}', '#{8}', '#{9}', '#{16}', '\\?{8}'),
        'North Carolina': ('#{1,12}',),
        'North Dakota': ('\\?{3}#{6}', '#{9}'),
        'Ohio': ('\\?#{4,8}', '\\?{2}#{3,7}', '#{8}'),
        'Oklahoma': ('\\?#{9}', '#{9}'),
        'Oregon': ('#{1,9}',),
        'Pennsylvania': ('#{8}',),
        'Rhode Island': ('#{7}', '\\?#{6}'),
        'South Carolina': ('#{5,11}',),
        'South Dakota': ('#{6,10}', '#{12}'),
        'Tennessee': ('#{7,9}',),
        'Texas': ('#{7,8}',),
        'Utah': ('#{4,10}',),
        'Vermont': ('#{8}', '#{7}a'),
        'Virginia': ('\\?#{8,11}', '#{9}'),
        'Washington': ('(\\?{1,7}[\\?|#|*]{5,11}){12}',),
        'West Virginia': ('#{7}', '\\?{1,2}#{5,6}'),
        'Wisconsin': ('\\?#{13}',),
        'Wyoming': ('#{9,10}',)
    }

    def drivers_license(self, state: str = None):
        state = state or self.random_element(self.states.keys())
        return self.bothify(
            self.generator.parse(self.random_element(self.states.get(state))),
            letters=string.ascii_uppercase
        )
