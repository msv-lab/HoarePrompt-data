(N, M, C) = map(int, raw_input().split())
B = map(int, raw_input().split())
ans = 0
for i in range(0, N):
    A = map(int, raw_input().split())
    tmp = [A[m] * B[m] for m in range(M)]
    if sum(tmp) + C > 0:
        ans += 1
print(ans)