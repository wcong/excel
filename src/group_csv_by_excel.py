#!/usr/bin/env python
#encoding=utf8

import xlwt    
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class conf:
    destination = 'test.xls'
    group = []
    # 设置 dir 会覆盖 group
    groupDir = './' 

def group( myConf = conf()):
    
    file = xlwt.Workbook( encoding = 'utf-8' )

    if myConf.groupDir != None:
        myConf.group = os.listdir( myConf.groupDir ) 
    for i in myConf.group:
        fileName = getFileName( i )
        table = file.add_sheet(fileName)
        soloFile = open( myConf.groupDir + '/' +i,'r') 
        i =0
        for line in soloFile:
            j =0
            lineData = line.split("\t")   
            for data in lineData:
                table.write(i,j,data) 
                j +=1 
            i+=1
        soloFile.close()
    file.save( myConf.destination )

def getFileName(path):
    split = path.split('/')
    fileName = split[len(split) -1]
    split = fileName.split('.')
    split = split[0:len(split)-1]
    return '.'.join(split)

myConf = conf()
myConf.destination = 'test.xls'
myConf.groupDir = '../test';
group( myConf )
