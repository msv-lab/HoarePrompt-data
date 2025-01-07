(n, m) = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
ops = []
for i in range(n - 1):
    for j in range(m - 1):
        if A[i][j] == 1 and A[i + 1][j] == 1 and (A[i][j + 1] == 1) and (A[i + 1][j + 1] == 1):
            continue
        if A[i][j] == 1 or A[i + 1][j] == 1 or A[i][j + 1] == 1 or (A[i + 1][j + 1] == 1):
            ops.append((i + 1, j + 1))
if len(ops) > 2500:
    print(-1)
else:
    print(len(ops))
    for op in ops:
        print(op[0], op[1])