#!/usr/bin/env python
# encoding: utf-8


"""
@version: V1.0
@author: '爸爸'
@license: *** Licence 
@contact: 15801095153@163.com
@site: http://www.***.com
@software: PyCharm
@file: filenames.py
@time: 2018/5/28 22:13
"""
import os

def getfilepath():
    filepath = os.getcwd()
    # print filepath
    filepath = os.path.join(filepath, r'data')
    # print filepath
    return filepath

def getfilenames():
    filepath = getfilepath()
    '''filenames = [x for x in os.listdir(os.path.dirname(filepath)) if os.path.isfile(x)]'''
    filenames = []

    for x in os.listdir(filepath):
        # print x
        filenames.append(os.path.join(filepath, x))
        # print filenames[0]
    return filenames
