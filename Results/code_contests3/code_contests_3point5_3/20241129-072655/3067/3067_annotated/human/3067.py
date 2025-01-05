#coding:utf-8

N,Q=map(int, raw_input().split())
S=raw_input()
P=[0]*(N+1)
for i in range(N):
    if i==0:
        P[0]=0
        continue
    if S[i-1:i+1]=="AC":
        P[i]=P[i-1]+1
    else:
        P[i]=P[i-1]
for _ in range(Q):
    l,r=map(int, raw_input().split())
    print(P[r-1]-P[l-1])