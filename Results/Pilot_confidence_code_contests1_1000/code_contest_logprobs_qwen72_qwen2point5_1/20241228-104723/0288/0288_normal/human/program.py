import os 
import sys
from sys import stdin, stdout

dp = {}

def fib(n):
    res = -1
    
    if n in dp:
        res = dp[n]
    elif n == 1:
        res = 1
    elif n == 2:
        res = 1
    else:
        res = fib(n-1) + fib(n-2)
    dp[n] = res
    return res

line = stdin.readline()
N = int(line)
fib(N)
res = ''
for i in range(N):
    if i+1 in dp.values():
        res = res + 'O'
    else:
        res = res + 'o'
print(res)
