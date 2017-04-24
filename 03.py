#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：一个正整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

import math

# method1
for i in range(1,10000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if (x*x == i+100) and (y*y == i+268):
        print i

print '=========== method2 ============'   
# method2
for i in range(10000):
    x = math.sqrt(i+100)
    y = math.ceil(i+100)
    #print ('i = ,x = , y =', i, x, y)
    if ((math.sqrt(i+100) == math.ceil(math.sqrt(i+100))) and (math.sqrt(i+268) == math.ceil(math.sqrt(i+268)))):
        print i

print '=========== method3 ============'
for i in range(10000):
    x = (math.sqrt(i+100))%1
    y = (math.sqrt(i+268))%1
    if x==0 and y==0:
        print i

print '=========== method4 ============'
for num in range(0,int(math.sqrt(10001 + 100))):
    
    if math.ceil(math.sqrt(num * num + 168)) == math.sqrt(num * num + 168):
        if num * num > 100 :  # 保证正整数
            print(num * num - 100)
