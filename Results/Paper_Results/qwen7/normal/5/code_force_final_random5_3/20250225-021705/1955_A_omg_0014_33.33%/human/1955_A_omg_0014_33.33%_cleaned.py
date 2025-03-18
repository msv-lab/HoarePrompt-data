n = int(input())
for i in range(n):
    (a, b, c) = map(int, input().split())
    d = c / 2
    if a * b < a * d:
        print(a * b)
    else:
        print(round(a * d))