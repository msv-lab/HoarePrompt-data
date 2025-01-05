def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = [max(a[i], a[i + 1]) for i in range(n - 1)]
        b.sort()
        print(b[0] - 1)

solve()
