import pandas as pd
from data_process import SQLReader
import argparse
from utils.auto_mail import auto_mail
from tqdm import tqdm
import os


def choice_best_fund():
    """
    选择最优的基金数据，既要有高收益，又可以抗风险。
    区分短期（近一月）、中期（近半年）、长期（近两年）
    1. 选出收益率最高的前100名，
    2. 从1中选出最大回撤最小的前20名，
    3. 从2中选出波动率最小的前5名。
    :return:
    """
    fund_info = SQLReader(args.database, config_path=args.config_path)
    money_fund_rank = fund_info.read_money_fund_rank()
    money_fund_rank.sort_values(by=['近1月', '近3月'], ascending=False, inplace=True)
    return money_fund_rank.iloc[:10]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='fund_analyse',  # 程序名
        description='analyse fund info.',  # 描述
    )

    parser.add_argument('--config_path', default=os.path.dirname(__file__) + r"\config.json", type=str)
    parser.add_argument('--database', default="fund_data", type=str)
    args = parser.parse_args()
    am = auto_mail(args.config_path)

    df = choice_best_fund()
    am.send_email_df("test01", df)
