#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :ch6_6.py
@Description  :
@Date         :2022/06/19 14:54:46
@Author       :Arctic Little Pig
@version      :1.0
'''

s_dict = {102: '张三', 105: '李四', 109: '王五'}

print('---遍历键---')
for s_id in s_dict.keys():
    print(f'学号: {s_id}')

print('---遍历值---')
for s_name in s_dict.values():
    print(f'学生: {s_name}')

print('---遍历键:值---')
for s_id, s_name in s_dict.items():
    print(f'学号: {s_id} -学生: {s_name}')
