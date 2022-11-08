#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :practice1.py
@Description  :
@Date         :2022/06/17 23:12:38
@Author       :Arctic Little Pig
@version      :1.0
'''

i = 999
r = 0
s = 0
t = 0

# for i in range(999, 99, -1):
for i in range(100, 1000):
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == (r ** 3 + s ** 3 + t ** 3):
        print(f"i = {i}")
    i += 1
