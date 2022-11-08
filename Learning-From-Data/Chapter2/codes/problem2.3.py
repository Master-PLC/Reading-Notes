#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :problem2.3.py
@Description  :
@Date         :2022/02/08 14:55:38
@Author       :Arctic Little Pig
@version      :1.0
'''

import argparse

import matplotlib.pyplot as plt


def plot_helper(Situation=1):
    plt.scatter([1, 2], [0, 0])

    if Situation == 1:
        plt.scatter([0, 3, 4], [0, 0, 0])
    elif Situation == 2:
        plt.scatter([3, 4], [0, 0])

    plt.plot([0.5, 0.5], [-1, 1], color='red')
    plt.plot([2.5, 2.5], [-1, 1], color='red')
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--Situation', type=int, default=1,
                        help='type of situation')
    config = parser.parse_args()

    plot_helper(config.Situation)
