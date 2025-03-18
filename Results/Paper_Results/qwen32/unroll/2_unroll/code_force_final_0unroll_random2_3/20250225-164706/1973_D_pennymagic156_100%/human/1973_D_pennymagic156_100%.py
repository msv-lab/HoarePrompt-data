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
    n, k = readInts()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        v = readInt()
        if v == n:
            v = i
            break
 
    for i in range(1, n // k + 1):
        # k cuts
        cnt, l = k, 1
        while cnt and l < n + 1:
            print(f'? {l} {i * v}', flush=True)
            l = readInt() + 1
            cnt -= 1
        if cnt == 0 and l == n + 1:
            print(f'! {i * v}', flush=True)
            readInt()
            return
    print('! -1', flush=True)
    readInt()
    return
 
 
for _ in range(int(input())):
    solve()