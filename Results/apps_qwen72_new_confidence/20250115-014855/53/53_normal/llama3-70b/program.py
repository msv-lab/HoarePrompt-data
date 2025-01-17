def count_games(n):
    x = 1
    games = 0
    while games < n:
        x *= 2
        games += x // 2
    if games > n:
        x //= 2
        games -= x // 2
    while games <= n:
        yield x
        x += 2
        games += x // 2

n = int(input())
res = list(count_games(n))
if not res:
    print(-1)
else:
    for i in res:
        print(i)
