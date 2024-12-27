# -*- coding: utf-8 -*-

n,m = map(int,raw_input().split())

students = [map(int,raw_input().split()) for _ in range(n)]
checkpoints = [map(int,raw_input().split()) for _ in range(m)]

#%%

for a,b in students:
    idx = -1
    dist = 10**9
    for j in range(m):
        c,d = checkpoints[j]
        manhat = abs(a-c)+abs(b-d)
        if manhat < dist:
            dist = manhat
            idx = j+1
    print(idx)