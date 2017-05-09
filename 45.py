#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：统计 1 到 100 之和。

a = [x for x in range(1, 101)]
b = (a[0] + a[-1]) * (len(a) // 2)
if len(a) % 2 != 0:
    b += a[(len(a) - 1) // 2]
print(b)
