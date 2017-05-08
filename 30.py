#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

a = int(raw_input("请输入一个数字:\n"))
x = str(a)
flag = True
print 'x[-1] = ', x[-2] 
for i in range(len(x)/2):
    print i
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print "%d 是一个回文数!" % a
else:
    print "%d 不是一个回文数!" % a
