N, M = map(int, raw_input().split())
A = map(int, raw_input().split())

AX = [0]
s = 0
for a in A:
    s += a
    AX.append(s)

result = 0
for i in range(1, N+1):
    for j in range(i, N+1):
        if (AX[j] - AX[i-1]) % M == 0:
            result += 1
print(result)
