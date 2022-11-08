#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :ch5_1_3.py
@Description  :
@Date         :2022/06/17 22:15:01
@Author       :Arctic Little Pig
@version      :1.0
'''

import argparse

parser = argparse.ArgumentParser(description="Demo of if-else structure.")
parser.add_argument('-s', '--score', default=100)
args = parser.parse_args()

score = int(args.score)

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade = " + grade)
