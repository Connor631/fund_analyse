from datetime import date
import holidays


class DateParser(object):
    def __init__(self):
        pass

    @staticmethod
    def parse_date_year(d: str):
        dt = date.fromisoformat(d)
        return dt.year

    @staticmethod
    def parse_date_month(d: str):
        dt = date.fromisoformat(d)
        return dt.month

    @staticmethod
    def parse_date_week(d: str):
        dt = date.fromisoformat(d)
        return dt.isocalendar()[1]

    @staticmethod
    def parse_date_weekday(d: str):
        dt = date.fromisoformat(d)
        return dt.isoweekday()

    @staticmethod
    def parse_date_day(d: str):
        dt = date.fromisoformat(d)
        return dt.day

    @staticmethod
    def parse_date_holiday(d: str):
        cn_holidays = holidays.country_holidays('CN')
        return int(d in cn_holidays)
