import sys
import random
from collections import Counter
import functools as ft

print = lambda x: sys.stdout.write(str(x) + "\n")
input = lambda: sys.stdin.readline().strip()

t = int(input())



def good(k, a):
    if k == 1:
        return True

    first = None
    for i in range(len(a)):
        if i < k-1:
            continue
        i1 = i
        i2 = i - k + 1
        num = 0
        for j in range(maxbit):
            ones = psums[i1][j]
            if i2 > 0:
                ones -= psums[i2-1][j]
            if ones > 0:
                num = num | (1 << j)

        if first is None:
            first = num
        else:
            if first != num:
                return False

    return True



for _ in range(t):
    n,  = map(int, input().split())
    a = list(map(int, input().split()))
    #a = [1,2,5]
    #n = 3

    maxbit = len(str(bin(max(a)))[2:])

    psums = [ [0 for i in range(maxbit)] for _ in range(n)]

    #print(maxbit)

    for i in range(n):
        ai = str(bin(a[i]))[2:].zfill(maxbit)
        for j, ch in enumerate(ai):
            if i == 0:
                psums[i][maxbit-j-1] = 1 if ch == '1' else 0
                continue
            if ch == '0':
                psums[i][maxbit-j-1] = psums[i-1][maxbit-j-1]
            else:
                psums[i][maxbit-j-1] = psums[i-1][maxbit-j-1]+1

    #print(psums)
    #sys.exit(0)


    l = 1
    r = n
    while l<r:
        m = (r+l)>>1
        #print(f" trying if good for {m}, {a}")
        if good(m, a):

            r = m
        else:
            l = m+1

    print(r)

