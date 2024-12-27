# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:16:16 2017

@author: wb
"""

list=raw_input()
length=len(list)
lendo=len(list)/2


ans=0
for i in range(0,lendo):
    if list[i]!=list[length-1-i]:
        ans=ans+1

 
if (ans<=1):
    print("YES")
else:
    print("NO")