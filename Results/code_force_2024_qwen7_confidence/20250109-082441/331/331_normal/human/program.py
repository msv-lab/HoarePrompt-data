import sys
 
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))

N = 500010
l,r,lp,rp = [0]*N,[0]*N,[0]*N,[0]*N


T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    lcnt,rcnt = 0,0
    for i in range(n):
        l[i+1]=r[i+1]=0
        if s[i]=='<': l[i+1]=1; lcnt+=1; lp[lcnt]=lp[lcnt-1]+i+1
        else: r[i+1]=1; rcnt+=1; rp[rcnt]=rp[rcnt-1]+i+1
        l[i+1]+=l[i]
        r[i+1]+=r[i]
    for i in range(1, n+1):
        lright, rleft = r[i-1], l[n]-l[i]
        k = min(lright, rleft)
        if s[i-1]=='<':
            ans = i+2*(lp[l[i]+k]-lp[l[i]])-2*(rp[lright]-rp[lright-k])
            if rleft<lright:
                ans += n+1-2*(rp[lright-k]-rp[lright-k-1])
            print(ans,end=' ')
        else:
            ans = 2*(lp[l[i]+k]-lp[l[i]])-2*(rp[lright]-rp[lright-k])-i+n+1
            if lright<rleft:
                ans += 2*(lp[l[i]+k+1]-lp[l[i]+k])-n-1
            print(ans,end=' ')
    print()