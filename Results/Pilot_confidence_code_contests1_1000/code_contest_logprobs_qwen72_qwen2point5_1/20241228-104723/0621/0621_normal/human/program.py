import sys
le = sys.__stdin__.read().split("\n")[::-1]
n = int(le.pop())
N = 6#200001
pr = [True]*N
l = list(map(int,le.pop().split()))
r=1
def v(p):
    r2 = 20
    r1 = 20
    for a in l:
        lr=0
        while a%p==0:
            a//=p
            lr += 1
        r1,r2,x=sorted([lr,r1,r2])
        #print(a,lr,p)
        if r2==0:
            return 1

    return p**r2


for k in range(2,N):
    if pr[k]:
        r *= v(k)
        for i in range(2*k,N,k):
            pr[i]=False

print(r)
