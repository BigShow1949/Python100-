#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))
 
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print 'data error'
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print 'it is the %dth day.' % sum


print '================== method2 ==================='

year=int(raw_input("年：\n"))
month=int(raw_input("月：\n"))
day=int(raw_input("日：\n"))
months1=[0,31,60,91,121,152,182,213,244,274,305,335,366] #闰年
months2=[0,31,59,90,120,151,181,212,243,273,304,334,365] #平年

if ((year%4==0)and(year%100!=0)) or((year%100==0)and(year%400==0)):
	Dth=months1[month-1]+day
else:
	Dth=months2[month-1]+day
print "是该年的第%d天"%Dth
