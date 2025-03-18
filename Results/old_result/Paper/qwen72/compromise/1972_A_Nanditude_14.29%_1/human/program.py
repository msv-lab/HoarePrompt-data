# import sys
# sys.stdout = open('Div3/output.txt', 'w')
# sys.stdin = open('Div3/input.txt', 'r')
 
def priorityQueue(arr):
    return sorted(arr, reverse=True)
 
import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    cnt = 0
    i = 0
    j = 0
    while(i<n and j<n):
        if(b[j]<a[i]):
            a.pop(-1)
            a = a[:i] + [b[j]] + a[i+1:]
            cnt+=1
            j+=1
        else:
            i+=1
            j+=1
 
    print(cnt)