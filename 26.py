#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：利用递归方法求5!。

print '===================   method2  ==========================='
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1, x+1):
        r *= i
    return r

print op(4)

print '===================   method3  ==========================='
s=0
def fact(n):
   if n==1:
      return 1
   return n*fact(n-1)

print fact(4)




