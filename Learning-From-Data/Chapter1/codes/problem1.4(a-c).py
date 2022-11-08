#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :problem1.4(a-c).py
@Description  :
@Date         :2022/01/29 23:39:08
@Author       :Arctic Little Pig
@version      :1.0
'''

import sys

util_path = sys.path[0].split("\\")
util_path = "\\".join(util_path[:-2])
sys.path.append(util_path)

import matplotlib.pyplot as plt
import numpy as np
from utils.random_seed import seed_init

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def sepJudge(X, y, w):
    """
    判别函数，判断所有数据是否分类完成
    """
    n = X.shape[0]
    # 判断是否同号
    num = np.sum(X.dot(w) * y > 0)
    return num == n


def data(N, d, t=0.1):
    """
    生成N个d维点（不包括偏置项1），x1+...+xd>=t的点标记为+1，x1+...+xd<=-t的点标记为-1
    """
    X = []
    w = np.ones(d)
    while (len(X) < N):
        x = np.random.uniform(-1, 1, size=(d))
        if np.abs(x.dot(w)) >= t:
            X.append(x)

    X = np.array(X)
    y = 2 * (X.dot(w) > 0) - 1
    # 添加第一个分量为1
    X = np.c_[np.ones((N, 1)), X]

    return X, y


def PLA(N, d, t=0.1, r=1):
    """
    生成N个d维点（不包括偏置项1），x1+...+xd>=t的点标记为+1，x1+...+xd<=-t的点标记为-1，
        利用PLA更新，如果r=1，那么按照顺序取点，否则随机取点
    """
    X, y = data(N, d, t=t)

    # 记录次数
    iters = 0
    # 初始化w=[0, 0, 0]
    w = np.zeros(d + 1)
    # 数据数量
    n = X.shape[0]
    if r == 1:
        while not sepJudge(X, y, w):
            for i in range(n):
                if X[i, :].dot(w) * y[i] <= 0:
                    w += y[i] * X[i, :]
                    iters += 1
    else:
        while not sepJudge(X, y, w):
            i = np.random.randint(0, N)
            if X[i, :].dot(w) * y[i] <= 0:
                w += y[i] * X[i, :]
                iters += 1

    # 直线方程为w0+w1*x1+w2*x2=0,根据此生成点
    x1 = np.arange(-1, 1, 0.1)
    x2_g = (x1 * w[1] + w[0]) / (- w[2])

    # 原直线方程为x1+x2 = 0
    x2_f = - x1

    # 返回数据
    return x1, x2_g, x2_f, X, y, iters, w


def plot_helper(x1, x2_g, x2_f, X, y, iters, w, t=0):
    """
    作图函数
    """
    # 画出图像
    plt.scatter(X[y == 1][:, 1], X[y == 1][:, 2], c='r', s=1)
    plt.scatter(X[y == -1][:, 1], X[y == -1][:, 2], c='b', s=1)
    plt.plot(x1, x2_g, label=str(w[0])+" + " +
             str(w[1])+" * x1 + "+str(w[2])+" * x2 = 0")
    plt.plot(x1, x2_f, label="x1 + x2 = "+str(t))
    plt.title(u"经过"+str(iters)+u"次迭代收敛")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    seed_init()
    
    N = 20
    d = 2
    x1, x2_g, x2_f, X, y, iters, w = PLA(N, d)
    plot_helper(x1, x2_g, x2_f, X, y, iters, w)
