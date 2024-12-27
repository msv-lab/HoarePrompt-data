import sys,math
from fractions import gcd
from bisect import bisect_left, bisect
from collections import defaultdict
from io import BytesIO
sys.stdin = BytesIO(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')
n = int(input())
#s = input()
arr = [int(_) for _ in input().split()]

d = defaultdict(int)
for el in arr:
    d[el] += 1
arr = []
for k in d:
    arr.append(d[k])
arr.sort(reverse=True)
#print(arr)
m = arr[0]
while arr[0] > 0:
    cur = arr[0]
    cs = arr[0]
    j = 1
    while cur % 2 == 0 and j < len(arr) and arr[j] >= cur // 2:
        j += 1
        cur /= 2
        cs += cur
    m = max(m,cs)
    arr[0] -= 1
print(m)