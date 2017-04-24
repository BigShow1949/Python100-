#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：斐波那契数列。
# 程序分析：程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。


def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
# 输出了第10个斐波那契数列
print fib(10)



print ('===============  method2  ==================')
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)
print fib(9)

print ('===============  method3  ==================')
def fib(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs = [1,1]
    for i in range (2,n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
print fib(10)

