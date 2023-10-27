import pandas as pd
from data_loading import SQLReader
from feather_engineering import FeatureExtraction
import argparse
from tqdm import tqdm
import os
import matplotlib.pyplot as plt


def show_fund_earnings():
    loader = SQLReader(args.config_path)
    fund_money_fund_df = loader.read_fund_money_fund()
    for i in tqdm(fund_money_fund_df["基金代码"]):
        print(i)
        fund_hist_single_df = loader.read_fund_money_fund_detail_single(i)
        fund_hist_single_index_df = FeatureExtraction.add_date_with_index(fund_hist_single_df, "净值日期")
        fund_group = fund_hist_single_index_df.groupby(['year', 'month'])
        ym_sum_df = fund_group.sum()['每万份收益']
        return ym_sum_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='fund_analyse',  # 程序名
        description='analyse fund info.',  # 描述
    )
    parser.add_argument('--config_path', default=os.path.dirname(__file__) + r"\config.json", type=str)
    args = parser.parse_args()

    df = show_fund_earnings()
