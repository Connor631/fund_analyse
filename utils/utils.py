from sqlalchemy import URL
from sqlalchemy import create_engine
import sqlalchemy
import json
from loguru import logger
import pandas as pd


class sql_utils(object):
    def __init__(self, database, config_path="config.json"):
        with open(config_path, "r", encoding="utf8") as fp:
            config = json.load(fp)
        self.host = config["sql_config"]["host"]
        self.port = config["sql_config"]["port"]
        self.account = config["sql_config"]["account"]
        self.pwd = config["sql_config"]["pwd"]
        self.engine = self.create_engine(database)

    def create_engine(self, database):
        """
        建立数据库连接，并指定数据库
        """
        url_object = URL.create(
            "mysql+pymysql",
            username=self.account,
            password=self.pwd,
            host=self.host,
            port=self.port,
            database=database,
        )
        engine = create_engine(
            url_object, poolclass=sqlalchemy.pool.QueuePool, pool_size=10
        )
        return engine

    def writer(self, df, table, write_type):
        """
        写入sql数据库
        :param df: 待写入数据
        :param table: 写入表格
        :param write_type: 写入方式(replace/append)
        :return: None
        """
        try:
            conn = self.engine.connect()
            df.to_sql(
                table,
                conn,
                if_exists=write_type,
                index=False,
            )
            conn.close()
        except Exception as e:
            logger.error(table + " writing is not successful")
            logger.error(repr(e))

    def reader(self, sql_statement):
        """
        读取SQL数据
        :param sql_statement: sql读取
        :return:
        """
        try:
            conn = self.engine.connect()
            df = pd.read_sql(sql_statement, conn)
            conn.close()
            return df
        except Exception as e:
            logger.error(sql_statement + " reading is not successful")
            logger.error(repr(e))
