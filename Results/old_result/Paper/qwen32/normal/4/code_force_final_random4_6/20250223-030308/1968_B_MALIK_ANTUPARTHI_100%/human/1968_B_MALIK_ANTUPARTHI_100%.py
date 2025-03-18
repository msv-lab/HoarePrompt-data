a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    d=input()
    e=input()
    k=0
    for j in range(b):
        if d[j] in e[k:]:
            k=e[k:].index(d[j])+1+k
            if k==c or j==b-1:
                k=j+1
                break
        else:
            k=j
            break
    print(k)