#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :problem2.12.py
@Description  :
@Date         :2022/02/10 16:57:24
@Author       :Arctic Little Pig
@version      :1.0
'''

import matplotlib.pyplot as plt
import numpy as np


def f(N):
    return (8 / N * np.log(4 * ((2 * N) ** dvc + 1) / delta)) ** 0.5 - 0.05


if __name__ == "__main__":
    delta = 0.05
    dvc = 10
    N = 1

    while(True):
        if(f(N) <= 0):
            break
        else:
            N += 1

    print(f"满足精度要求和置信度要求的N为{N}")

    x = range(1, 1000)
    y = [f(i) for i in x]

    plt.plot(x, y)
    plt.title('epsilon-0.05')
    plt.show()
