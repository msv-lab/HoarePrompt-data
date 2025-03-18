t = int(input())
for T in range(t):
    bets = int(input())
    a = [int(x) for x in input().split()]
    prod = 1
    for i in range(bets):
        prod *= a[i]
    sumo = 0
    for i in range(bets):
        a[i] = prod // a[i]
        sumo += int(a[i])
    if sumo >= prod:
        print(-1)
    else:
        ans = ''
        for i in range(bets):
            ans += str(a[i]) + ' '
        print(ans)