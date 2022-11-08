#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :exercise2.5.py
@Description  :
@Date         :2022/02/05 13:46:26
@Author       :Arctic Little Pig
@version      :1.0
'''

import numpy as np


def m(n):
    return n + 1


def delta(N, epsilon):
    return 4 * m(2 * N) / (np.exp(N * (epsilon ** 2) / 8))


if __name__ == "__main__":
    N = 100
    epsilon = 0.1
    print(delta(100, 0.1))
