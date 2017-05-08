#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。

n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print '1! + 2! + 3! + ... + 20! = %d' % s


print '===================   method2  ==========================='
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1, x+1):
        r *= i
    return r
s = sum(map(op, l))
print '1! + 2! + 3! + ... + 20! = %d' % s


print '===================   method3  ==========================='
s=0
def fact(n):
   if n==1:
      return 1
   return n*fact(n-1)

for n in  range(1,21):
   a=fact(n)
   s+=a
# print s
print sum(map(fact, l))


print '===================   method4  ==========================='
s = 0
for i in range(1, 21):
    r = 1
    for j in range(1, i+1):
        r *= j
    s += r
print(s)


