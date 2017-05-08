#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：按逗号分隔列表。

L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print 's1 = ', s1


#对序列进行操作
seq1 = ['hello','good','boy','doiido']
print ':'.join(seq1)

#对字符串进行操作
seq2 = "helle good boy doiido"
print ':'.join(seq2)

#对元组进行操作
seq3 = ('hello','good','boy','doiido')
print ':'.join(seq3)

#对字典进行操作
seq4 = {'hello':1,'good':2,'boy':3,'doiido':4}
print ':'.join(seq4)

#合并目录
import os
print os.path.join('/hello/','good/boy/','doiido')
