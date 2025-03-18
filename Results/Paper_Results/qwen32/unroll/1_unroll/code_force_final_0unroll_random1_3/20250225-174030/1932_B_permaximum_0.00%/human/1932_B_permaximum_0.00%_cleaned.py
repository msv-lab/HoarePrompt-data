t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    year = 0
    for ai in a:
        year += year % ai or ai
    print(year)