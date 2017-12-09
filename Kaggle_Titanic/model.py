# coding=utf-8

import xgboost as xgb
import numpy as np

from settings import train_data_path,test_data_path

def load_data(path):
    tmp = np.loadtxt(path,dtype=np.str, delimiter=",")
    data = tmp[1:, 1:]  # 加载数据部分
    label = tmp[1:, 1].astype(np.float)  # 加载类别标签部分
    return data, label  # 返回array类型的数据