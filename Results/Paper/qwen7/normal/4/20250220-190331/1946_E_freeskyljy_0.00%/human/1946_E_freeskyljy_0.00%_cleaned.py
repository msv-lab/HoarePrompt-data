input = sys.stdin.readline
MOD = int(1000000000.0 + 7)

def func_1():
    (N, M1, M2) = map(int, input().split())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    if L[-1] != R[0]:
        return 0
    if L[0] != 1 or R[0] != N:
        return 0
    if M1 > 1 and M2 > 1 and (L[-2] == R[1]):
        return 0
    ans = math.comb(N - 1, L[-1] - 1)
    cur = M1 - 2
    if M1 > 1:
        nums_left = L[-1] - 2
        i = L[-1] - 1
        while i > 1:
            if i == L[cur]:
                cur -= 1
            else:
                ans = ans * nums_left % MOD
            nums_left -= 1
            i -= 1
    nums_left = N - R[0] - 1
    if M2 > 1:
        cur = 1
        i = R[0] + 1
        while i < N:
            if i == R[cur]:
                cur += 1
            else:
                ans = ans * nums_left % MOD
            nums_left -= 1
            i += 1
    return ans
for _ in range(int(input())):
    print(func_1())