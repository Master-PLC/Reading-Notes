#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :ch5_2_1_2.py
@Description  :
@Date         :2022/06/17 22:25:59
@Author       :Arctic Little Pig
@version      :1.0
'''

i = 0

while i * i < 10:
    i += 1
    print(f"{i} * {i} = {i * i}")
else:
    print("While over!")
