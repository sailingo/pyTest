#!/usr/bin/python3
# -*- coding: utf-8 -*-
#========================================================================
# Author: shilg
# Email: shilinguo@126.com
# File Name: test.py
# Description: 
#   
# Edit History: 
#   2021-07-02    File created.
#========================================================================
#1,1,2,3,5,8,13,21,34,55

import keyboard

def foo():
    a, b = 0, 1
    while b < 100:
        a, b = b, a+b
        print ("print:",a)

end foo()
