N = int(input())
A = map(int, raw_input().split())

k = 0
g = 0

for i in range(N):
    if A[i] % 2 == 0:
        g += 1
    else:
        k += 1

if k == 0 or (g != 0 and k % g == 0 and k / g == 2):
    print('Yes')
else:
    print('No')