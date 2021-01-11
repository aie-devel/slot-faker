from faker.providers.date_time import Provider as BaseProvider
import dateparser
from datetime import date


class Provider(BaseProvider):
    def human_date_range(self, nl_desc: str):
        switch = {
            '-': lambda x, y: (x - y, x),
            '+': lambda x, y: (x + y, x),
            '+-': lambda x, y: (x - y, x + y)
        }

        pattern, start, operand, *end = nl_desc.split()
        if '-' in operand and '+' in operand:
            operand = '+-'
        start_date = dateparser.parse(start)
        relative_end_date = ' '.join(end)
        diff = start_date - dateparser.parse(relative_end_date)
        return switch.get(operand)(start_date, diff)

    def date_this_week(self, before_today=True, after_today=False):
        today = date.today()
        this_week_start = today.replace(day=(today.day - today.weekday()))
        next_week_start = this_week_start.replace(day=(today.day + (7 - today.weekday())))

        if before_today and after_today:
            return self.date_between_dates(
                this_week_start, next_week_start)
        elif not before_today and after_today:
            return self.date_between_dates(today, next_week_start)
        elif not after_today and before_today:
            return self.date_between_dates(this_week_start, today)
        else:
            return today
