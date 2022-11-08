#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :ch5_1_2.py
@Description  :
@Date         :2022/06/17 22:10:19
@Author       :Arctic Little Pig
@version      :1.0
'''


import argparse

parser = argparse.ArgumentParser(description="Demo of if-else structure.")
parser.add_argument('-s', '--score', default=100)
args = parser.parse_args()

score = int(args.score)

if score >= 60:
    if score >= 85:
        print("您真优秀! ")
    else:
        print("您的成绩还可以，仍需继续努力! ")
else:
    print("您需要加倍努力! ")
