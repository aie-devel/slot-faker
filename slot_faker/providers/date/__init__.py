from datetime import date
import random
import dateparser
from faker.providers.date_time import Provider as BaseProvider


class Provider(BaseProvider):
    def _suffix(self, d):
        return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

    def _custom_strftime(self, t):
        formats = (
            '%B {S}, %Y',
            '%B {S}',
            'the {S} of %B'
        )

        format = self.random_element(formats)

        return t.strftime(format).replace('{S}', f"{str(t.day)}{self._suffix(t.day)}")

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

    def date_next_week(self):
        return self.date_this_week(before_today=False, after_today=True)

    def date_last_week(self):
        return self.date_this_week(before_today=True, after_today=False)

    def date_within_months(self, months: int = 6, before_today=True, after_today=True):
        today = date.today()

        plus_months = today.month + (months % 12)
        plus_years = today.year + (months // 12)

        if plus_months > 12:
            plus_months -= 12
            plus_years += 1

        next_months = today.replace(
            year=plus_years,
            month=plus_months
        )

        minus_months = today.month - (months % 12)
        minus_years = today.year - (months // 12)

        if minus_months < 1:
            minus_months += 12
            minus_years -= 1

        last_months = today.replace(
            year=minus_years,
            month=minus_months
        )

        if before_today and after_today:
            return self.date_between_dates(
                last_months, next_months
            )
        elif not before_today and after_today:
            return self.date_between_dates(today, next_months)
        elif not after_today and before_today:
            return self.date_between_dates(last_months, today)
        else:
            return today

    def date_next_six_months(self):
        return self.date_within_months(before_today=False, after_today=True)

    def date_last_six_months(self):
        return self.date_within_months(before_today=True, after_today=False)

    def date_next_month(self):
        return self.date_within_months(months=1, before_today=False, after_today=True)

    def date_last_month(self):
        return self.date_within_months(months=1, before_today=True, after_today=False)

    def date_day(self, before_today=True, after_today=True, start_date=None, end_date=None):

        today = date.today()
        start_date = start_date or today.replace(year=(today.year - 25))
        end_date = end_date or today.replace(year=(today.year + 25))

        if before_today and after_today:
            day = self.date_between_dates(start_date, end_date)
        elif not before_today and after_today:
            day = self.date_between_dates(today, end_date)
        elif not after_today and before_today:
            day = self.date_between_dates(start_date, today)
        else:
            day = today

        return self._custom_strftime(day)

    def date_within_days(self, days: int = 14, before_today=True, after_today=True):
        today = date.today()
        next_days = today.replace(
            day=(today.day + days)
        ) if (today.day + days <= 28) else today.replace(
            month=(today.month + 1), day=((today.day + days) % 28)
        )
        last_days = today.replace(
            day=(today.day - days)
        ) if (today.day - days > 0) else today.replace(
            day=1
        )

        if before_today and after_today:
            return self.date_between_dates(
                last_days, next_days
            )
        elif not before_today and after_today:
            return self.date_between_dates(today, next_days)
        elif not after_today and before_today:
            return self.date_between_dates(last_days, today)
        else:
            return today

    def date_next_decade(self):
        return self.date_this_decade(before_today=False, after_today=True)

    def date_last_decade(self):
        return self.date_this_decade(before_today=True, after_today=False)

    def date_next_month(self):
        return self.date_this_month(before_today=False, after_today=True)

    def date_next_fortnight(self):
        return self.date_within_days(before_today=False, after_today=True)

    def date_last_fortnight(self):
        return self.date_within_days(before_today=True, after_today=False)

    def date_last_year(self):
        return self.date_within_months(months=12, before_today=True, after_today=False)

    def date_last_three_months(self):
        return self.date_within_months(months=3, before_today=True, after_today=False)

    def date_next_three_months(self):
        return self.date_within_months(months=3, before_today=False, after_today=True)

    def date_last_two_years(self):
        return self.date_within_months(months=24, before_today=True, after_today=False)

    def date_next_two_years(self):
        return self.date_within_months(months=24, before_today=False, after_today=True)

    def date_last_three_years(self):
        return self.date_within_months(months=36, before_today=True, after_today=False)

    def date_next_three_years(self):
        return self.date_within_months(months=36, before_today=False, after_today=True)

    def date_last_five_years(self):
        return self.date_within_months(months=60, before_today=True, after_today=False)

    def date_next_five_years(self):
        return self.date_within_months(months=60, before_today=False, after_today=True)

    def date_six_to_three_months_ago(self):
        today = date.today()

        six_months_ago_month = today.month - 6
        six_months_ago_year = today.year
        if six_months_ago_month < 1:
            six_months_ago_month += 12
            six_months_ago_year -= 1

        three_months_ago_month = today.month - 3
        three_months_ago_year = today.year
        if three_months_ago_month < 1:
            three_months_ago_month += 12
            three_months_ago_year -= 1

        six_months_ago = today.replace(
            month=six_months_ago_month,
            year=six_months_ago_year
        )

        three_months_ago = today.replace(
            month=three_months_ago_month,
            year=three_months_ago_year
        )

        return self.date_between_dates(six_months_ago, three_months_ago)

    def date_six_to_three_months_from_now(self):
        today = date.today()

        six_months_from_now_month = today.month + 6
        six_months_from_now_year = today.year
        if six_months_from_now_month > 12:
            six_months_from_now_month -= 12
            six_months_from_now_year += 1

        three_months_from_now_month = today.month + 3
        three_months_from_now_year = today.year
        if three_months_from_now_month > 11:
            three_months_from_now_month -= 12
            three_months_from_now_year += 1

        six_months_from_now = today.replace(
            month=six_months_from_now_month,
            year=six_months_from_now_year
        )

        three_months_from_now = today.replace(
            month=three_months_from_now_month,
            year=three_months_from_now_year
        )

        return self.date_between_dates(three_months_from_now, six_months_from_now)

    def day_of_month(self):
        options = [
            *[f"{i}{self._suffix(i)}" for i in range(32)],
            'first',
            'last'
        ]
        day = self.random_element(options)
        if random.getrandbits(1):
            return f"the {day}"
        return f"the {day} of the month"