#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :problem1.5(a-d).py
@Description  :
@Date         :2022/01/30 00:04:04
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


def Adaline(eta, w0, iteration=1000):
    """
    w0为分界线的法向量，w0=[0] + [1] * d，这里d = 2
    """

    # 记录次数
    T = 0
    w = np.zeros(d + 1)
    # print(X_train.dot(w) * y_train)
    while not sepJudge(X_train, y_train, w) and T < iteration:
        i = np.random.randint(0, N1)
        s = X_train[i, :].dot(w)
        a = s * y_train[i]
        if a <= 1:
            w += eta * (y_train[i] - s) * X_train[i, :]
            T += 1

    # 计算错误率
    num = np.sum(X_test.dot(w) * y_test <= 0)

    print("η为"+str(eta)+"时测试错误率为"+f"{num/N2:.5f}")

    # 直线方程为w0+w1*x+w2*y=0,根据此生成点
    X3 = np.arange(-1, 1, 0.1)
    Y3 = np.array([(x*w[1]+w[0])/(-w[2]) for x in X3])

    # 目标函数
    X4 = np.arange(-1, 1, 0.1)
    Y4 = np.array([(x*w0[1]+w0[0])/(-w0[2]) for x in X4])

    # 画出图片
    plt.scatter(X_train[y_train == 1][:, 1],
                X_train[y_train == 1][:, 2], c='r', s=1)
    plt.scatter(X_train[y_train == -1][:, 1],
                X_train[y_train == -1][:, 2], c='b', s=1)
    plt.plot(X3, Y3, label=str(w[0]) + " + "+str(w[1])+" * x + "+str(w[2])+" * y = 0")
    plt.plot(X4, Y4, label=str(w0[0]) + " + "+str(w0[1])+" * x + "+str(w0[2])+" * y = 0")
    plt.title(u"经过"+str(T)+u"次迭代")
    # 设置坐标范围
    # plt.xticks(np.arange(0,10))
    # plt.yticks(np.arange(0,10))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    seed_init()

    # 训练数据
    N1 = 100
    # 测试数据
    N2 = 10000
    # 数据维度
    d = 2
    # 生成数据
    X_train, y_train = data(N1, d)
    X_test, y_test = data(N2, d)

    Eta = [1, 0.1, 0.01, 0.001]
    for eta in Eta:
        Adaline(eta, [0, 1, 1])
