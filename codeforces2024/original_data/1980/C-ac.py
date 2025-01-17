import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())  
    a = input().split()  
    b = input().split()  
    k = int(input()) 
    d = input().split()  
    s=set()
    d1={}
    f=0
    for i in range(n):
        if b[i]!=a[i]:
            if b[i] in s:
                d1[b[i]]=d1.get(b[i], 0) + 1
            else:
                s.add(b[i])
                d1[b[i]]=1
    
    for i in range(k-1):
        if d[i] in s:
            d1[d[i]]=d1.get(d[i], 0) -1
    
    if d[-1] in s:
        d1[d[-1]]=d1.get(d[-1], 0) -1
        
    elif d[-1] in b:
        h=1
    else:
        f=1
    
    if f==1:
        print("NO")
    else:
        for key in d1.keys():
            if d1.get(key)<1:
                continue
            else:
                f=1
                break
        if f==1:
            print("NO")
        else:
            print("YES")