#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：暂停一秒输出。

import time

myD = {'one' : 1, 'two' : 2}
for key,value in dict.items(myD):
    print key, value
    time.sleep(1)
