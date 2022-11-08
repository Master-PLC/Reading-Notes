#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :problem2.7.py
@Description  :
@Date         :2022/02/09 20:59:59
@Author       :Arctic Little Pig
@version      :1.0
'''

import argparse
from math import e

import matplotlib.pyplot as plt


def bound1(N, d):
    return (N ** d) + 1


def bound2(N, d):
    return (e * N / d) ** d


def draw(d):
    n = list(range(1, 50))
    m1 = [bound1(i, d) for i in n]
    m2 = [bound2(i, d) for i in n]

    plt.plot(n, m1, label='bound in problem 2.5')
    plt.plot(n, m2, label='bound in problem 2.6')
    plt.legend()
    plt.title('d_vc='+str(d))
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dvc', type=int, default=2,
                        help='VC Dimension')
    config = parser.parse_args()

    draw(config.dvc)
