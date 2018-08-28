#!/usr/bin/env python
# encoding: utf-8


"""
@version: V1.0
@author: '爸爸'
@license: *** Licence 
@contact: 15801095153@163.com
@site: http://www.***.com
@software: PyCharm
@file: analise.py
@time: 2018/5/28 23:03
"""
import datawrite
import collections
def getmax(yearconten_int):
    return max(yearconten_int)


def getaverage(monthdata):
    tatal = 0.0
    num = 0
    for i in monthdata:
        tatal += i
        num += 1
    return tatal/num


def analise(filenames,conten):
    tataldays = len(conten) - 1
    # print 'tataldays = ',tataldays #tatal days
    tatalyears = tataldays / 365
    # print 'tatalyears = ', tatalyears # tatal years
    # print ' type conten[0] =  ',type(conten[0])
    # print conten[0]
    startyear = int(conten[0][0:4])
    # print 'startyear = ', startyear
    startday = 1
    yearconten = []
    # max_year_precipitation = 0
    twelvemonth = collections.OrderedDict([('jan', 31), ('fre', 28), ('mar', 31), ('apr', 30), ('may', 31), ('jun', 30), ('jul', 31), ('aug', 31), ('sep', 30), ('oct', 31), ('nov', 30), ('dec', 31)])
    # OrderedDict([('c', 1), ('d', 2), ('b', 4)])
    # twelvemonth = {'jan': 31, 'fre': 28, 'mar': 31, 'apr': 30, 'may': 31, 'jun': 30, 'jul': 31, 'aug': 31, 'sep': 30,'oct': 31, 'nov': 30, 'dec': 31}

    maxcotent = ''
    mothonaverage = ''

    for year in range(tatalyears):
        cycleflag = int(startyear) % 4
        if(cycleflag == 0):#截取366
            yearconten = conten[startday:startday+366]
            startday += 366
            yearconten_float = [float(i) for i in yearconten]
            '''get max every year '''
            maxcotent += filenames.split('\\')[-1]
            maxcotent += '\n'+ str(getmax(yearconten_float))+ '\n'
            '''get max every year '''
            '''get max every month '''
            tempdays = 0
            for mon in twelvemonth.iterkeys():
                monthdata = yearconten_float[tempdays:tempdays + twelvemonth[mon]]
                tempdays += twelvemonth[mon]
                mothonaverage += filenames.split('\\')[-1] + ' ' + mon + ' ' + str(getaverage(monthdata)) + '\n'
                print getaverage(monthdata)
                print mon


        else:
            # 截取365
            yearconten = conten[startday:startday + 365]
            startday += 355
            yearconten_float = [float(i) for i in yearconten]
            '''get max every year '''
            maxcotent += filenames.split('\\')[-1]
            maxcotent += '\n' + str(getmax(yearconten_float)) +'\n'
            '''get max every year '''
            '''get max every month '''
            twelvemonth['fre'] = 29
            tempdays = 0
            for mon in twelvemonth.iterkeys():
                monthdata = yearconten_float[tempdays:tempdays + twelvemonth[mon]]
                tempdays += twelvemonth[mon]
                mothonaverage += filenames.split('\\')[-1] + ' ' + mon +' '+ str(getaverage(monthdata)) + '\n'
                print getaverage(monthdata)
                print mon

        startyear += 1
    return maxcotent, mothonaverage



