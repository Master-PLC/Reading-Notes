#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :problem2.9.py
@Description  :
@Date         :2022/02/09 23:22:21
@Author       :Arctic Little Pig
@version      :1.0
'''

import matplotlib.pyplot as plt
from scipy.special import comb


def mH(N, d):
    result = 0
    k = min(d, N-1)
    for i in range(k + 1):
        result += comb(N - 1, i)

    return 2 * result


if __name__ == "__main__":
    x = range(1, 41)
    d = 10
    y = [mH(i, d) / (2 ** i) for i in x]

    plt.plot(x, y)
    plt.xlabel('N')
    plt.ylabel('mH(N)/2**N')
    plt.show()

    print([mH(i, d) / (2 ** i) for i in [10, 20, 40]])
