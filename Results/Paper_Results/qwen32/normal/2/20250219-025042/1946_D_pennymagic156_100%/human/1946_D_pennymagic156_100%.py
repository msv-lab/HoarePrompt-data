import sys
input = sys.stdin.readline
 
def readList():
    return list(map(int, input().split()))
def readInt():
    return int(input())
def readInts():
    return map(int, input().split())
def readStr():
    return input().strip()
 
# BF-OB5, EC, DB, CC, CL
def solve():
    n, x = readInts()
    a = readList()
    t, ans = [], -1
    for i in range(29, -1, -1):
        u, v = (x >> i) & 1, sum([(val >> i) & 1 for val in a])
        if u == v == 0:
            continue
            
        if u == 0:
            if v % 2:
                return ans
            else:
                op = ai = 0
                for val in a:
                    op ^= (val >> i) & 1
                    ai ^= val
                    if not op:
                        t.append(ai)
                        ai = 0
                a, t = t, []
 
        else:
            if v % 2:
                continue
            elif v:
                op = cnt = 0
                for val in a:
                    op ^= (val >> i) & 1
                    if not op:
                        cnt += 1
                ans = max(ans, cnt)
            else:
                break
    return max(ans, len(a))
 
 
for _ in range(int(input())):
    print(solve())