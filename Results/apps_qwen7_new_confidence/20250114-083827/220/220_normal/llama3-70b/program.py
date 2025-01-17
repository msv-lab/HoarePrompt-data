n, m, s, d = map(int, input().split())
obstacles = list(map(int, input().split()))

obstacles.sort()
i = 0
x = 0
while x < m:
    if i < n and obstacles[i] <= x + s:
        while i < n and obstacles[i] <= x + s:
            i += 1
        if i == n or obstacles[i] > x + d:
            print("IMPOSSIBLE")
            exit()
        else:
            print("RUN", obstacles[i] - x)
            x = obstacles[i]
    else:
        if x + s > m:
            print("IMPOSSIBLE")
            exit()
        else:
            print("RUN", s)
            x += s
    while i < n and obstacles[i] <= x + d:
        i += 1
    if i < n:
        print("JUMP", obstacles[i] - x)
        x = obstacles[i]
    else:
        print("RUN", m - x)
        break
