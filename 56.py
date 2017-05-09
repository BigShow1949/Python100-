#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 题目：画图，学用circle画圆形。　

if __name__ == '__main__':
    from Tkinter import *

    root = Tk()
    Tk()
    # 创建一个Canvas，设置其背景色为白色
    cv = Canvas(root, bg ='white')
    cv.create_rectangle(10,10,110,110, outline = 'red', width = 1, dash = 10, fill = 'green', stipple = 'gray12')
    #cv.pack()
    #root.mainloop()


    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
        k += j
        j += 0.3
    mainloop()
