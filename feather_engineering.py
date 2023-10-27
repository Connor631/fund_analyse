# Feature Selection（特征选择）、Feature Extraction（特征提取）和Feature construction（特征构造）
from utils.data_parser import DateParser
import pandas as pd


class FeatureExtraction(object):
    def __init__(self):
        pass

    @staticmethod
    def extract_date(a: pd.Series):
        year = a.map(DateParser.parse_date_year)
        month = a.map(DateParser.parse_date_month)
        day = a.map(DateParser.parse_date_day)
        week = a.map(DateParser.parse_date_week)
        weekday = a.map(DateParser.parse_date_weekday)
        holiday = a.map(DateParser.parse_date_holiday)
        df = pd.DataFrame(
            {"date": a, "year": year, "month": month, "day": day, "week": week, "weekday": weekday, "holiday": holiday})
        df.set_index("date", inplace=True)
        return df

    @staticmethod
    def add_date_with_index(df_with_date, date_cols_name: str):
        date_extract_df = FeatureExtraction.extract_date(df_with_date[date_cols_name])
        df_with_date.set_index(date_cols_name, inplace=True)
        return df_with_date.join(date_extract_df)
