#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# method1
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and i!=k and j!=k):
                print i,j,k

# method2
d = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and i!=k and j!=k):
                d.append([i,j,k])
print "total count:", len(d)
print d

# method3
list_num = [1,2,3,4]
list = [i*100 + j*10 + k for i in list_num for j in list_num for k in list_num if
        j!=i and j!=k and i!=k]
print len(list)

# method4


            
