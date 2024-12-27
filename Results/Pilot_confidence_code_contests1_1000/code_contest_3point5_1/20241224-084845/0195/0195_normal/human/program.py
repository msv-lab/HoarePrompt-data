from sys import stdin
from bisect import *

n, a = int(input()), [int(x) for x in stdin.readline().split()]
dis = sorted(set(a))
for i in dis:
    if a[i - 1] != i:
        print(-1)
        exit()

tem = []
for i in range(n):
    tem.append(bisect_left(dis, a[i]) + 1)

print('%d\n%s\n%s' % (max(tem), ' '.join(map(str, tem)), ' '.join(map(str, dis))))
