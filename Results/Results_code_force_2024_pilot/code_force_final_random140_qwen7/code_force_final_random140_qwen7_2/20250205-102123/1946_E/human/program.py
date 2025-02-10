import sys
import math
input = sys.stdin.readline
MOD = int(1e9+7)
 
def comb(n1, n2):
    if n1 == n2:
        return 1
    if n2 == 0:
        return 1
    f1 = 1
    f2 = 1
    f3 = 1
    for i in range(1, n1+1):
        if i == n2+1:
            f2 = f1
        if i == n1 - n2 + 1:
            f3 = f1
        f1 = (f1*i)%MOD
    a = pow((f2*f3)%MOD, -1, MOD)
    return (f1*a)%MOD
 
def solve():
    N, M1, M2 = map(int, input().split())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    # if N == 1:
    #     return 1
    if L[-1] != R[0]:
        return 0
    if L[0] != 1 or R[-1] != N:
        return 0
    if M1 > 1 and M2 > 1 and L[-2] == R[1]:
        return 0
    ans = comb(N-1, L[-1]-1)
    # left
    cur = M1 - 2
    if M1 > 1:
        nums_left = L[-1] - 2
        i = L[-1] - 1
        while i > 1:
            if i == L[cur]:
                cur -= 1
            else:
                ans = (ans*nums_left)%MOD
            nums_left -= 1
            i -= 1
    # right
    nums_left = N - R[0] - 1
    if M2 > 1:
        cur = 1
        i = R[0] + 1
        while i < N:
            if i == R[cur]:
                cur += 1
            else:
                ans = (ans*nums_left)%MOD
            nums_left -= 1
            i += 1
    return ans
 
for _ in range(int(input())):
    print(solve())