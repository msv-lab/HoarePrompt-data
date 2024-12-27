# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:04:29 2017

@author: wb
"""
from __future__ import print_function
import math


a={}
list=raw_input().split()
n=int(list[0])
m=int(list[1])
cnt=0
cl_n=int(math.sqrt(n))
if cl_n<2:
    cl_n=2
for i in range(2,cl_n+1):
    while n%i==0:
        cnt=cnt+1
        a[cnt]=i;
        n=n/i
    
if cnt>=m:
   jl=cnt-m
   ans=1
   for i in range(1,jl+2):
       ans=ans*a[i]
   for i in range(jl+2,cnt+1):
       print(a[i],' ',end='')
   print(ans)
else:
    print('-1')