from math import log2

def solve(n):
    digits = int(log2(n))
    ans = list(range(1, digits+1))
    rev = []
    pos = 1
    while n:
        if n & 1: rev.append(pos)
        pos += 1
        n >>= 1
    rev.pop()

    return ans + rev[::-1]

for _ in range(int(input())):
    n = int(input())
    ans = solve(n)
    print(len(ans))
    print(*ans)