import pandas as pd
from data_loading import SQLReader
import argparse
from tqdm import tqdm
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='fund_analyse',  # 程序名
        description='analyse fund info.',  # 描述
    )
    parser.add_argument('--config_path', default=os.path.dirname(__file__) + r"\config.json", type=str)
    args = parser.parse_args()

