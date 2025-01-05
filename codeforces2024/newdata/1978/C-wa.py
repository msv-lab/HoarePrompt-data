def list_p(n,k):
    k=k//2
    l=list(range(1,n+1))
    for i in range(n-1,-1,-1):
        if k==0:
            return l
        if 1+i>k:
            x=l[-1]
            l.pop(-1)
            l.insert(-k,x)
            return l
        k=k-i+1
        x=l[-1]
        l.pop(-1)
        l.insert(0,x)

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
    # print(l)
    p(l)
    return

T=int(input())
for i in range(T):solve()