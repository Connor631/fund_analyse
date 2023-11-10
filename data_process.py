import pandas as pd
from utils.utils import sql_utils
from loguru import logger


class SQLReader(sql_utils):
    def __init__(self, database, config_path):
        sql_utils.__init__(self, database, config_path)
        logger.add("./log/fund_analyse.log", rotation="10 MB")

    def read_fund_all(self):
        return self.reader("select * from fund_all_list")

    def read_money_fund_rank(self):
        return self.reader("select * from fund_money_fund_rank")

    def read_money_fund_statistics(self):
        return self.reader("select * from fund_money_fund_statistics")
