t = int(input())
for _ in range(t):
    n = int(input())
    plays = []
    clears = []
    for _ in range(n):
        p, c = map(int, input().split())
        plays.append(p)
        clears.append(c)
    ok = True
    for i in range(1, n):
        if plays[i] < plays[i-1] or clears[i] < clears[i-1]:
            ok = False
            break
        if clears[i] > plays[i]:
            ok = False
            break
    print("YES" if ok else "NO")
