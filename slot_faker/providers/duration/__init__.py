from faker.providers import BaseProvider
import dateparser
import humanize

class Provider(BaseProvider):

    carrier_phrases = (
        'for about {}',
        'for approximately {}',
        'for approx. {}',
        'for around about {}',
        'maybe {}',
        'give or take {}',
        'round about {}',
        'probably {} or so',
        'going on {}, give or take',
        'since about {} ago'
    )

    def approximate_duration(self, nl_desc: str):
        span = dateparser.parse(nl_desc)

        carrier = self.random_element(self.carrier_phrases)
        return carrier.format(humanize.naturaldelta(span))