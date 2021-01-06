from faker.providers import BaseProvider
from datetime import datetime
from time import mktime
import random


class Provider(BaseProvider):
    formats = (
        '%-I:%M %p',
        '%-I:%M',
        '%-H:%M',
        '%-I o\'clock'
    )

    hour_parts = {
        'quarter': (0, 15, 30, 45),
        'half': (0, 30)
    }

    open = datetime.now().astimezone().replace(hour=8, minute=0)
    close = datetime.now().astimezone().replace(hour=17, minute=0)

    def _personalize(self, time: str):
        if 'M' in time:
            if random.getrandbits(1):
                time = time.lower()
                if random.getrandbits(1):
                    time = time.replace('m', '.m.')
            if random.getrandbits(1):
                time = time.replace(' ', '')
        return time

    def business_datetime(self):
        timestamp = random.randint(
            mktime(self.open.timetuple()),
            mktime(self.close.timetuple())
        )
        return datetime.fromtimestamp(timestamp)

    def business_time(self, nearest: str = None):
        pattern = self.random_element(self.formats)
        bt = self.business_datetime()
        if nearest and (parts := self.hour_parts.get(nearest)):
            m = self.random_element(parts)
            bt = bt.replace(minute=m)
        return self._personalize(
            bt.strftime(pattern)
        )
