#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :problem2.11.py
@Description  :
@Date         :2022/02/09 23:37:49
@Author       :Arctic Little Pig
@version      :1.0
'''

import argparse

import numpy as np


def f(N, delta):
    return np.sqrt(8 / N * np.log(4 * (2 * N + 1) / delta))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, default=100,
                        help='number of training samples')
    config = parser.parse_args()

    delta = 0.1

    print(f(config.N, delta))

