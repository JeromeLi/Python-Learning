#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sample_newbie_00.py
@Time    :   2022/04/30 22:59:42
@Author  :   Jerome
@Version :   1.0
@Contact :   jerome.lzh@gmail.com
@License :   GPL-3.0
@Desc    :   None
'''

# here put the import lib
import asyncio
from time import sleep

async def func1():
    print('func1:1')
    await asyncio.sleep(2)
    print('func1:2')

async def func2():
    print('func2:1')
    await asyncio.sleep(2)
    print('func2:2')

func1()
func2()
