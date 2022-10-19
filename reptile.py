#!/usr/bin/python
# -*- coding: utf-8 -*-
#========================================================================
# Author: shilg
# Email: shilinguo@126.com
# File Name: reptile.py
# Description: 
#   
# Edit History:
#   2020-07-03    File created.
#========================================================================
import requests

if __name__ == '__main__':
    target = 'http://gitbook.cn'
    req = requests.get(url=target)
    print(req.text)
    print(req.text)
