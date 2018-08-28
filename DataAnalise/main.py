#!/usr/bin/env python
# encoding: utf-8


"""
@version: V1.0
@author: '爸爸'
@license: *** Licence 
@contact: 15801095153@163.com
@site: http://www.***.com
@software: PyCharm
@file: main.py
@time: 2018/5/28 20:32
"""
import dataread, analise,datawrite

def main():
    tatalconten = dataread.dataread()
    tatalout = ()
    maxcotent = ''
    monthaverage = ''
    for (filename, conten) in tatalconten.items():#/station
        # print type(conten)
        tatalout = analise.analise(filename, conten)
        maxcotent += tatalout[0]
        monthaverage += tatalout[1]



    # datawrite.writemax_year_precipitation(maxcotent)
    datawrite.writewrite_month_average(monthaverage)
    # print 'maxcotent = ', maxcotent
main()
