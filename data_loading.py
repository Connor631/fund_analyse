import pandas as pd
from utils.utils import SQLManager


class SQLReader(object):
    def __init__(self, config_path):
        self.sql_conn = SQLManager.sql_conn(config_path)

    def read_fund_all(self):
        return pd.read_sql("select * from fund_all_list", self.sql_conn)

    def read_fund_money_fund(self):
        return pd.read_sql("select * from fund_money_fund_daily_list", self.sql_conn)

    def read_fund_money_fund_detail_single(self, code: str):
        money_single_df = pd.read_sql(f"select * from fund_money_fund_detail where code = {code}", self.sql_conn)
        money_single_df["每万份收益"] = pd.to_numeric(money_single_df["每万份收益"], errors='coerce')
        money_single_df["7日年化收益率"] = pd.to_numeric(money_single_df["7日年化收益率"], errors='coerce')
        return money_single_df

    def read_fund_money_fund_rank(self):
        return pd.read_sql("select * from fund_money_fund_rank", self.sql_conn)
