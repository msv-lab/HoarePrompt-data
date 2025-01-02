from sys import stdin
n,k = map(int,stdin.readline().split())
a = map(int,stdin.readline().split())
di = {}
for i in a:
    di[i] = di.get(i,0) + 1
ma = 0
for i in di:
    ma  = max(ma,di[i])
print (len(set(a)) * ( (ma + k-1)/k)) - n