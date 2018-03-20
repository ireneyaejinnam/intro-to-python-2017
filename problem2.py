#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:07:14 2017

@author: ireneyaejinnam
"""

"""
(c): (a) until the first occurence of a substring in s then stops (b) len(s)-len(substring)+1 in the worst case.
However, the worst case for (a) will also be len(s)-len(substring)+1 (if the substring is at the very end),
so the algorithm in part (b) won't be making more comparisons than the worst case scenario for (a). 
"""


#(a) write the function that does the same thing as the find method
def find(s,substring):
    target = 0
    if substring in s:
        for x in s:
            if (target+len(substring)-1) < len(s):
                if substring[0] == x:
                    if s[target:target+len(substring)] == substring:
                        return target
            target += 1
    else:
        return -1

find(s,substring)


#(b) Without using the existing find method, write a function find_multi(s, substring)
def multi_find(s,substring):
    target = 0
    series = []
    if substring in s:
        for x in s:
            if (target+len(substring)-1) < len(s):
                if substring[0] == x:
                    if s[target:target+len(substring)] == substring:
                        series.append(target)
            target += 1
        return series
    else:
        return series

multi_find(s,substring)

