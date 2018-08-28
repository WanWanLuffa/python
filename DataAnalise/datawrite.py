#!/usr/bin/env python
# encoding: utf-8


"""
@version: V1.0
@author: '爸爸'
@license: *** Licence 
@contact: 15801095153@163.com
@site: http://www.***.com
@software: PyCharm
@file: datawrite.py
@time: 2018/5/28 20:32
"""
import os

def writemax_year_precipitation ( writemax_year_precipitation):
    filewritepath = os.getcwd()
    filewritepath = os.path.join(filewritepath, r'maxresult.txt')
    if not os.path.exists(filewritepath):
        with open(filewritepath,'w') as fileopen:
            fileopen.write(writemax_year_precipitation)
            # print writemax_year_precipitation
    else:
        with open(filewritepath,'w') as fileopen:
            fileopen.write(writemax_year_precipitation)
            # print writemax_year_precipitation

def writewrite_month_average( write_month_average):
    filewritepath = os.getcwd()
    filewritepath = os.path.join(filewritepath, r'average.txt')
    if not os.path.exists(filewritepath):
        with open(filewritepath,'w') as fileopen:
            fileopen.write(write_month_average)
            # print average_month_precipitation
    else:
        with open(filewritepath,'w') as fileopen:
            fileopen.write(write_month_average)
            # print average_month_precipitation

