import sys
from functools import lru_cache
sys.setrecursionlimit(100000000)
def read():
    return sys.stdin.readline().strip()
def ii():
    return int(read())
def il():
    return list(map(int,read().split()))
t=ii()
def solve():
    n,m,x=il()
    ans={x}
    for _ in range(m):
        r,c=read().split()
        r=int(r)
        temp=set()
        for q in ans:
            if c=='0' or c=='?':
                temp.add((q+r)%n)
            if c=='1' or c=='?':
                temp.add((q-r)%n)
        ans=temp
    if 0 in ans:
        ans.discard(0)
        ans.add(n)
    print(len(ans))
    print(*ans)
for i in range(t):
    solve()