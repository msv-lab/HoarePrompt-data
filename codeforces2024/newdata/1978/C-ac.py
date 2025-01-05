def list_p(n,k):
    k=k//2
    l=list(range(1,n+1))
    c=0
    for i in range(n,-1,-2):
        c+=1
        if k==0:
            return l
        if k<i-1:
            return r_ret(c,k,l)
        k=k-i+1
        l=ret(c,l)

def r_ret(c,k,l):
    x,y=l[-c],l[-c-k]
    l[-c],l[-c - k]=y,x
    return l

def ret(c,l):
    x,y=l[-c],l[c-1]
    l[c-1],l[-c]=x,y
    return l


def tf():
    n,k=map(int,input().split())
    if k%2:
        return 0,0
    if n%2:
        max_k=(n**2-1)//2
    else:
        max_k=(n**2)//2
    if max_k<k:
        return 0,0
    return n,k

def p(l):
    print('YES')
    for i in l:
        print(i,end=' ')
    print()
    return

def solve():
    n,k=tf()
    if n==0:
        print('NO')
        return
    l=list_p(n,k)
    p(l)
    return

T=int(input())
for i in range(T):solve()