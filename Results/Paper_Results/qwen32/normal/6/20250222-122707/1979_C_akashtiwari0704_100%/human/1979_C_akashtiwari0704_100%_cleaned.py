t = int(input())
for T in range(t):

    def lcm(l):
        g = 1
        for i in range(len(l)):
            g = g * l[i] // gcd(g, l[i])
        return g
    bets = int(input())
    a = [int(x) for x in input().split()]
    prod = lcm(a)
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