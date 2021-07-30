#!/usr/bin/python
# -*- coding: utf-8 -*-
# ========================================================================
# Author: findstr
# Email: findstr@sina.com
# File nAME: write.py
# Description:
#
# Edit History:
#   2019-06-18    File created.
# ========================================================================


def func0(a):
    a += 1
    print('this is func0')


def func1(x):
    x += 1
    return x


def func2():
    return 'Hello,world', ('python', 'php'), [1, 3, 4], func0(2)


def get_list(x, y):
    return [x, y]

# 参数组参数传入


def get_list2(*var):
    return var

    return args

# 递归


def enlarge(n):
    if n < 1008:
        print(n)
        return enlarge(n+1)


print("test")

enlarge(8)

#u = display(a=1,b=2,c=3)
# print(u)
