#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :exercise2.2.py
@Description  :
@Date         :2022/02/04 21:04:47
@Author       :Arctic Little Pig
@version      :1.0
'''

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def f(X):
    return X + 2 ** np.floor(X / 2)


def g(X):
    return X ** 2 / 2 + X / 2 + 1


def plot_helper(X, y1, y2):
    """
    作图函数
    """
    # 画出图像
    plt.plot(X, y1, label="N + 2^{floor(N/2)}")
    plt.plot(X, y2, label="N^2/2 + N/2 + 1")
    plt.xlabel("N")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    X = np.arange(1, 20, 0.1)
    y1 = f(X)
    y2 = g(X)
    plot_helper(X, y1, y2)
