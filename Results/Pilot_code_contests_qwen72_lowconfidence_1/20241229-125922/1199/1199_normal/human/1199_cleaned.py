t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    A = map(int, raw_input().split())
    A.reverse()
    F = [0] * n
    M = [0] * n
    F[0] = A[0]
    if n == 1:
        print(F[0])
        continue
    F[1] = A[1]
    for i in range(2, n):
        M[i] = min(F[i - 1], F[i - 2])
        F[i] = min(A[i] + M[i - 1], A[i] + A[i - 1] + M[i - 2])
    print(F[-1])