#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :ch5_2_1_3.py
@Description  :
@Date         :2022/06/17 22:29:12
@Author       :Arctic Little Pig
@version      :1.0
'''

i = 0

while i * i < 10:
    i += 1
    if i == 3:
        break
    print(f"{i} * {i} = {i * i}")
else:
    print("While over!")
