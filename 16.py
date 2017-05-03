#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：输出指定格式的日期。
# 程序分析：使用 datetime 模块。

import datetime
if __name__ == '__main__':

    print(datetime.date.today().strftime('%d/%m/%Y'))

    birthDay = datetime.date(1941, 1, 5)

    print(birthDay.strftime('%d/%m/%Y'))

    birthNextDay = birthDay + datetime.timedelta(days=1)

    print(birthNextDay.strftime('%d/%m/%Y'))

    firstBirthDay = birthDay.replace(year = birthDay.year + 1)

    print(firstBirthDay.strftime('%d/%m/%Y'))


