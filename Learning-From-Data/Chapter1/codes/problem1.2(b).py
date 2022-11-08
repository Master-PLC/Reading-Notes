#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :problem1.2(b).py
@Description  :
@Date         :2022/01/29 22:46:53
@Author       :Arctic Little Pig
@version      :1.0
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    x = np.arange(-1, 1, 0.1)
    y1 = np.array([-1/3 - 2/3 * i for i in x])
    y2 = np.array([-1/3 - 2/3 * i for i in x])
    plt.plot(x, y1, label='w=[1,2,3]T')
    plt.plot(x, y2, label='w=-[1,2,3]T')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
