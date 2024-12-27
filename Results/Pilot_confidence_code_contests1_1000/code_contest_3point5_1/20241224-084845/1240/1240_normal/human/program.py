import sys
testing = len(sys.argv) == 4 and sys.argv[3] == "myTest"
if testing:
    cmd = sys.stdout
    from time import time
    start_time = int(round(time() * 1000)) 
    input = open(sys.argv[1], 'r').readline
    sys.stdout = open(sys.argv[2], 'w')
else:
    input = sys.stdin.readline
mod = 10**9+7
# from math import ceil
# from collections import defaultdict as dd
# from heapq import *
############ ---- I/O Functions ---- ############
def intin():
    return(int(input()))
def intlin():
    return(list(map(int,input().split())))
def chrin():
    s = input()
    return(list(s[:len(s) - 1]))
def strin():
    s = input()
    return s[:len(s) - 1]
def intlout(l, sep=" "):
    print(sep.join(map(str, l)))

def main():
    n = intin()
    a = intlin()
    b = [bin(x)[:1:-1] for x in a]
    maxK = max([len(x) for x in b])
    bcnt = [0]*maxK
    for i in xrange(n):
        x = b[i]
        for k in xrange(len(x)):
            if x[k] == '1':
                bcnt[k] += 1
    kpowb = [(((1<<k)%mod)*bcnt[k])%mod for k in xrange(maxK)]
    summ = sum(kpowb)
    ans = 0
    for j in xrange(n):
        x = b[j]
        tmp = 0
        tmp2 = 0
        for k in xrange(len(x)):
            tmp += kpowb[k]
            tmp2 -= kpowb[k]
        k += 1
        tmp2 += summ%mod
        tmp2 += (a[j]%mod)*n
        ans += ((tmp%mod)*(tmp2%mod))%mod
        ans %= mod
    # print(ans)
    return(ans)
            


if __name__ == "__main__":
    ans = []
    for _ in xrange(intin()):
        ans.append(main())
        # main()
        # print("YES" if main() else "NO")
    intlout(ans,'\n')
    # main()

    if testing:
        sys.stdout = cmd
        print(int(round(time() * 1000))  - start_time)