#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：按相反的顺序输出列表的值。

a = ['one', 'two', 'three']
for i in a[::-1]:
	print i


print '输入列表格式为：1,2,3,4'
s=input()
print type(s)
a=list(s)
print a[::-1]
