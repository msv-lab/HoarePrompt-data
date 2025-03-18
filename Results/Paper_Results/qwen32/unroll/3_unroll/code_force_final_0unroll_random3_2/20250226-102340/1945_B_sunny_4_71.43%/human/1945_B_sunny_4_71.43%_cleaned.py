t = int(input())
for _ in range(t):
    (a, b, m) = map(int, input().split())
    A = int(m / a) + 1
    B = int(m / b) + 1
    print(A + B)