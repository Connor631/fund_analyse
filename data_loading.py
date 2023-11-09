import pandas as pd
from utils.utils import sql_utils
from loguru import logger


class SQLReader(sql_utils):
    def __init__(self, database):
        sql_utils.__init__(self, database)
        logger.add("./log/fund_analyse.log", rotation="10 MB")

    def read_fund_all(self):
        return self.reader("select * from fund_all_list")
