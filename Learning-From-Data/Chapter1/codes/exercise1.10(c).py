#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :exercise1.10(c).py
@Description  :
@Date         :2022/01/29 18:15:31
@Author       :Arctic Little Pig
@version      :1.0
'''

import sys

import matplotlib.pyplot as plt
import numpy as np
from utils.random_seed import seed_init

util_path = sys.path[0].split("\\")
util_path = "\\".join(util_path[:-2])
sys.path.append(util_path)


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

    epsilon = np.arange(0, 2, 0.01)
    size = epsilon.shape[0]

    Z1 = np.zeros(size)
    Z2 = np.zeros(size)
    Z3 = np.zeros(size)

    # 计算P(|u-v|>epsilon)
    for i in range(size):
        for j in range(11):
            if abs(j / 10.0 - 0.5) > epsilon[i]:
                Z1[i] += Y1[j]
                Z2[i] += Y2[j]
                Z3[i] += Y3[j]
    Z1 = Z1 / m
    Z2 = Z2 / m
    Z3 = Z3 / m

    # Hoeffding上界值
    Z = np.array([2 * np.exp(-2*(i**2)*10) for i in epsilon])

    # 作图
    plt.plot(epsilon, Z, label=u"Hoeffding上界")
    plt.plot(epsilon, Z1, label=u"P(|v1-u|)")
    plt.plot(epsilon, Z2, label=u"P(|vrand-u|)")
    plt.plot(epsilon, Z3, label=u"P(|vmin-u|)")
    plt.xlabel(u'epsilon')
    plt.ylabel(u'概率')
    plt.legend()
    plt.show()
