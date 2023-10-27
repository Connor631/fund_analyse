from sqlalchemy import URL
from sqlalchemy import create_engine
import json


class SQLManager(object):
    @staticmethod
    def sql_conn(path):
        # 数据库配置文件
        with open(path, "r", encoding="utf8") as fp:
            config = json.load(fp)
        # 建立数据库url地址并连接
        url_object = URL.create(
            "mysql+pymysql",
            username=config["sql_config"]["account"],
            password=config["sql_config"]["pwd"],  # plain (unescaped) text
            host=config["sql_config"]["host"],
            port=config["sql_config"]["port"],
            database="fund_data",
        )
        engine = create_engine(url_object)
        return engine
