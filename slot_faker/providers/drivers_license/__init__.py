from slot_faker.providers import BaseProvider
import string
import itertools
import re

def permutate(poss_list):
    if all(isinstance(item, str) for item in poss_list):
        return poss_list if len(poss_list) > 1 else poss_list[0]
    if all(isinstance(item, (list, tuple)) for item in poss_list):
        if len(poss_list) == 1:
            return poss_list
        elif len(poss_list) == 2:
            return [
                ''.join(product)
                for product in itertools.product(*poss_list)
            ]
        elif len(poss_list) > 2:
            return [
                ''.join(product)
                for product in itertools.product(poss_list[0], permutate(poss_list[1:]))
            ]
        else:
            raise ValueError


def get_char_set(chars: list, min: int, max: int = None):
    min = int(min)
    max = int(max) or min
    max += 1
    char_set = []
    for i in range(min, max):
        char_set.extend(permutate(list(itertools.repeat([*chars], i))))
    return char_set



class Provider(BaseProvider):

    states = {
        'Alabama': ('#{1,8}',),
        'Alaska': ('#{1,7}',),
        'Arizona': ('?{1,1}#{8,8}', '#{9,9}'),
        'Arkansas': ('#{4,9}',),
        'California': ('?{1,1}#{7,7}',),
        'Colorado': ('#{9,9}', '?{1,1}#{3,6}', '?{2,2}#{2,5}'),
        'Connecticut': ('#{9,9};',),
        'Delaware': ('#{1,7}',),
        'District of Columbia': ('#{7,7}', '#{9,9}'),
        'Florida': ('?{1,1}#{12,12}',),
        'Georgia': ('#{7,9}',),
        'Hawaii': ('?{1,1}#{8,8}', '#{9,9}'),
        'Idaho': ('?{2,2}#{6,6}?{1,1}', '#{9,9}'),
        'Illinois': ('?{1,1}#{11,11}', '?{1,1}#{12,12}'),
        'Indiana': ('?{1,1}#{9,9}', '#{9,9}', '#{10,10}'),
        'Iowa': ('#{9,9}', '#{3,3}?{2,2}#{4,4}'),
        'Kansas': ('?{1,1}#{1,1}?{1,1}#{1,1}?{1,1}', '?{1,1}#{8,8}', '#{9,9}'),
        'Kentucky': ('?{1,1}#{8,8}', '?{1,1}#{9,9}', '#{9,9}'),
        'Louisiana': ('#{1,9}',),
        'Maine': ('#{7,7}', '#{7,7}?{1,1}', '#{8,8}'),
        'Maryland': ('?{1,1}#{12,12}',),
        'Massachusetts': ('?{1,1}#{8,8}', '#{9,9}'),
        'Michigan': ('?{1,1}#{10,10}', '?{1,1}#{12,12}'),
        'Minnesota': ('?{1,1}#{12,12}',),
        'Mississippi': ('#{9,9}',),
        'Missouri': ('?{1,1}#{5,9}', '?{1,1}#{6,6}R{1,1}', '#{8,8}?{2,2}', '#{9,9}?{1,1}', '#{9,9}'),
        'Montana': ('?{1,1}#{8,8}', '#{13,13}', '#{9,9}', '#{14,14}'),
        'Nebraska': ('?{1,1}#{6,8}',),
        'Nevada': ('#{9,9}', '#{10,10}', '#{12,12}', 'X{1,1}#{8,8}'),
        'New Hampshire': ('#{2,2}?{3,3}#{5,5}',),
        'New Jersey': ('?{1,1}#{14,14}',),
        'New Mexico': ('#{8,8}', '#{9,9}'),
        'New York': ('?{1,1}#{7,7}', '?{1,1}#{18,18}', '#{8,8}', '#{9,9}', '#{16,16}', '?{8,8}'),
        'North Carolina': ('#{1,12}',),
        'North Dakota': ('?{3,3}#{6,6}', '#{9,9}'),
        'Ohio': ('?{1,1}#{4,8}', '?{2,2}#{3,7}', '#{8,8}'),
        'Oklahoma': ('?{1,1}#{9,9}', '#{9,9}'),
        'Oregon': ('#{1,9}',),
        'Pennsylvania': ('#{8,8}',),
        'Rhode Island': ('#{7,7}', '?{1,1}#{6,6}'),
        'South Carolina': ('#{5,11}',),
        'South Dakota': ('#{6,10}', '#{12,12}'),
        'Tennessee': ('#{7,9}',),
        'Texas': ('#{7,8}',),
        'Utah': ('#{4,10}',),
        'Vermont': ('#{8,8}', '#{7,7}A{1,1}'),
        'Virginia': ('?{1,1}#{8,11}', '#{9,9}'),
        'Washington': ('(?{1,7}[?#*]{5,11}){12,12}',),
        'West Virginia': ('#{7,7}', '?{1,2}#{5,6}'),
        'Wisconsin': ('?{1,1}#{13,13}',),
        'Wyoming': ('#{9,10}',)
    }

    def drivers_license(self, state: str = None):
        state = state or self.random_element(self.states.keys())
        #formats = self._get_formats(self.states.get(state))
        return 'FC18960'
        '''
        return self.bothify(
            self.generator.parse(formats),
            letters=string.ascii_uppercase
        )
        '''

    '''
    def _get_formats(self, format):
        results = []
        for part in format:
            parts = [
                subpart
                for subpart in re.split(r'[{,}]', part)
                if subpart
            ]
            batches = [parts[i:i+3] for i in range(0, len(parts), 3)]
            string_set = []
            for char, min, max in batches:
                char_set = get_char_set(char, min, max)
                char_set = [char_set[0][0], *char_set[1:]]
                string_set.append(char_set)
            results.extend(permutate(string_set))
        results = [
            strf if isinstance(strf, str) else *strf
            for strf in results
        ]
        return results
        '''
