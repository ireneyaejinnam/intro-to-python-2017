#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:25:39 2017

@author: ireneyaejinnam
"""


series = []
series.append([1])
rows = int(input("Enter the number of rows:"))

if rows > 1:
    series.append([1,1])
    for n in range(2,rows):  
        row_above = series[n-1]
        row_now = [1]
        for p in range(0,len(row_above)-1):
            row_now.append(row_above[p]+row_above[p+1])
        row_now.append(1)
        series.append(row_now)

x = len(series)

for i in range(0,x):
    for j in range(0, 2*(x-1-i)):
        print(" ", end = "")    
    for j in series[i]:	
        print (j, end = "   ")
    
    print()	
