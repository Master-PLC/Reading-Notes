#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :ch5_4.py
@Description  :
@Date         :2022/06/17 23:08:41
@Author       :Arctic Little Pig
@version      :1.0
'''

i = 100
r = 0
s = 0
t = 0

while i < 1000:
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == (r ** 3 + s ** 3 + t ** 3):
        print(f"i = {i}")
    i += 1
