from __future__ import print_function,division

def f():
    n=int(raw_input())
    #print(n)
    l=[int(raw_input()) for k in range(n)]
    li=[True]*10
    for k in l:
        li[k%10]=False
    k=0
    for i in range(n-1):
        if l[i] in l[i+1:]:
            k+=1
            r=0
            while not(li[r]):
                r+=1
            li[r]=False
            l[i]=10*(l[i]//10)+r
    print(k)
    for j in l:
        print(j)
for z in range(int(raw_input())):
    #print(z)
    f()
