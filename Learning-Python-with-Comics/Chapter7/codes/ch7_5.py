#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename     :ch7_5.py
@Description  :
@Date         :2022/06/19 15:38:37
@Author       :Arctic Little Pig
@version      :1.0
'''

# 一篇文章文本
wordstring = """
    it was the best of times it was the worst of times.
    it was the age of wisdom it was the age of foolishness.
"""

# 将标点符号替换
wordstring = wordstring.replace('.', '')

# 分割单词
wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    # 统计单词出现个数
    wordfreq.append(wordlist.count(w))

d = dict(zip(wordlist, wordfreq))
print(d)
