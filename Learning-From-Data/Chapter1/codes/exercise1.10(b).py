#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :exercise1.10(b).py
@Description  :
@Date         :2022/01/29 18:15:31
@Author       :Arctic Little Pig
@version      :1.0
'''

import sys

util_path = sys.path[0].split("\\")
util_path = "\\".join(util_path[:-2])
sys.path.append(util_path)

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb
from utils.random_seed import seed_init

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def simu(n):
    """
    首先模拟一次实验的结果，n表示硬币数量，1表示正面，0表示反面，最后返回的结果为正面的数量
    """
    # n个硬币，每个硬币投10次
    X = np.random.randint(0, 2, (n, 10))
    # 计算每个硬币正面的数量
    X1 = np.sum(X, axis=1)
    # 第一个元素
    y1 = X1[0]
    # 随机元素
    y2 = X1[np.random.randint(0, n)]
    # 最小值
    y3 = np.min(X1)
    return y1, y2, y3


def total(x):
    """
    计算正面的次数
    """
    s = 0
    for i in range(len(x)):
        s += i * x[i]
    return s


def f(k, n):
    """
    P(v<=k), n表示一共几个硬币
    """
    s = 0
    for i in range(k + 1, 11):
        s += comb(10, i) / (2**10)
    return 1 - s ** n


def g(k, n):
    """
    P(v=k)
    """
    return f(k, n) - f(k-1, n)


def h(n):
    s = 0
    for k in range(11):
        s += k / 10.0 * g(k, n)
    return s


if __name__ == "__main__":
    seed_init()

    # 记录正面硬币得分的具体情况，存入一个长度为11的列表，第i个元素表示得分为i的次数
    Y1 = [0] * 11
    Y2 = [0] * 11
    Y3 = [0] * 11
    # 硬币数量
    n = 1000
    # 实验次数
    m = 10000
    for i in range(m):
        y1, y2, y3 = simu(n)
        Y1[y1] += 1
        Y2[y2] += 1
        Y3[y3] += 1

    # 投硬币的总次数
    t = m * 10

    # (b)
    plt.bar(range(11), Y1)
    plt.title(u'C 1平均正面比例' + str(total(Y1) / t))
    plt.show()

    plt.bar(range(11), Y2)
    plt.title(u'C rand平均正面比例' + str(total(Y2) / t))
    plt.show()

    plt.bar(range(11), Y3)
    plt.title(u'C min平均正面比例' + str(total(Y3) / t))
    plt.show()

    print(h(1000))
