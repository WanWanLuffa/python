#!/usr/bin/env python
# encoding: utf-8


"""
@version: V1.0
@author: '爸爸'
@license: *** Licence 
@contact: 15801095153@163.com
@site: http://www.***.com
@software: PyCharm
@file: dataread.py
@time: 2018/5/28 20:29
"""
import filenames

def dataread():
    # print 'get in dataread'
    felsenamelist = filenames.getfilenames()
    tatalconten = {}
    i = 0
    tempconntenstr = ''
    for x in felsenamelist:
        i +=1
        # print x
        with open(x) as f:
            tempconntenstr = ''.join(f.readlines() ).strip('\n')
            tatalconten[x] = tempconntenstr.strip('\n').split('\n')
            # print x
    print "the number of file:", i
    return tatalconten
