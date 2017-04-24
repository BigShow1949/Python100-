#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：将一个列表的数据复制到另一个列表中。
# 程序分析：使用列表[:]。


a = [1, 2, 3]
b = a[:]
a = [2, 3, 4]
print 'a=', a
print 'b=', b

# 'list' object has no attribute 'copy'
print ('===============  method1  ==================')
import copy
a = {'a' : 11}
b = a.copy()
print b
