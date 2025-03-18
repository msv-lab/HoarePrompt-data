def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        [n, m] = [int(n), int(m)]
        ans = 0
        for b in range(1, min(n, m) + 1):
            ans = ans + n // b + 1
        print(ans)

