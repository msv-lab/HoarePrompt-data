import math

def listfullzero(n):
    list = [0] * n
    return list
n = int(input())
q = raw_input().split(' ');
i = 0;
res = 0
list = listfullzero(35)
while i < n:
    a = int(q[i])
    tmp = 0
    while a > 0:
        if a % 2:
            a = (a - 1) / 2
            tmp += 1
        else:
            a = a / 2
    list[tmp] += 1
    i += 1
i = 0
while i < 35:
    res += list[i] * (list[i] - 1) / 2
    i += 1
print(res)