# -*- coding: utf-8 -*-

n = input()
a = map(int,raw_input().split())

mod = 10**9+7
flg = [False]*n
      
for i in range(n):
    if(flg[a[i]]==False):
        flg[a[i]] = True
    elif(flg[a[i]-1]==False and a[i]-1>=0):
        flg[a[i]-1] = True
    
           
if(n%2==0):
    if(all(flg)):
        print(2**(n/2) % mod)
    else:
        print('0')
else:
    if(all(flg)):
        print(2**((n-1)/2) % mod)
    else:
        print('0')
        