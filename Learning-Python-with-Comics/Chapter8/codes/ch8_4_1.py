#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :ch8_4_1.py
@Description  :
@Date         :2022/06/29 15:18:15
@Author       :Arctic Little Pig
@version      :1.0
'''


def sum(*numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total


print(sum(100.0, 20.0, 30.0))  # 输出150.0
print(sum(30.0, 80.0))  # 输出110.0
