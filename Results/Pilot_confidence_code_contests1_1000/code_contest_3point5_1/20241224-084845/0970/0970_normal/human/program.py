from __future__ import absolute_import, division, print_function
from sys import *
inp = lambda : stdin.readline()

N = int(1e6)+30

def main():
    n = int(inp())
    l = [int(i) for i in inp().split()]
    d = [0 for i in range(N)]
    ans,m = 0,0
    for i in l:
        d[i] += 1
        m = max(m,i)
    for i in range(N-1):
        have = d[i]
        d[i+1] += d[i]//2
        if d[i]%2: ans += 1
    print(ans)


if __name__ == "__main__":
    main()