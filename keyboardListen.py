#!/usr/bin/python
# -*- coding: utf-8 -*-
#========================================================================
# Author: shilg
# Email: shilinguo@126.com
# File Name: command.py
# Description: 
#   
# Edit History: 
#   2021-08-19    File created.
#========================================================================
from pynput import keyboard
import time
# 导入线程库，因为监听键盘和鼠标都是阻塞的
import threading
 
isEnd = False
 

#cmd = 'sl'
#for i in range(10):
#    d = os.system(cmd)
#    print(d)
 
# 键盘按下执行的函数 使用try和except的原因是有特殊按键（功能键）
def keyboard_on_press(key):
    global isEnd
    try:
        print('字母键{0} press'.format(key.char))
    except AttributeError:
        print('特殊键{0} press'.format(key))
        if key == keyboard.Key.esc:
            isEnd = True
            return False
 
 
# 开启键盘监听的线程函数
def start_key_listen():
    with keyboard.Listener(on_press=keyboard_on_press) as KeyboardListener:
        KeyboardListener.join()
 
 
# 被中断的程序
def function():
    while True:
        if isEnd:
            return False
        print(0)
        time.sleep(1)
 
 
def main():
    # 创建、启动键盘监听线程
    t1 = threading.Thread(target=start_key_listen)
    t1.start()
 
    # 创建、启动鼠标监听线程
    t2 = threading.Thread(target=function)
    t2.start()
 
    # 等待线程结束
    t1.join()
    t2.join()
 
 
if __name__ == "__main__":
    main()
