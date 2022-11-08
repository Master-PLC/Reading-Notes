#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :problem2.1.py
@Description  :
@Date         :2022/02/06 21:49:06
@Author       :Arctic Little Pig
@version      :1.0
'''

import argparse

import numpy as np


def f(M, epsilon):
    return np.log(2 * M / delta)/(2 * epsilon ** 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--M', type=int, default=1, help='number of hypothesis')
    parser.add_argument('--epsilon', type=float,
                        default=0.05, help='error tolerance')
    config = parser.parse_args()

    delta = 0.03
    print(f(config.M, config.epsilon))
