def func_1(p):
    max_n = 100
    remaining_players = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cur_n = n
        while cur_n >= min(p):
            count = bisect.bisect_right(p, cur_n)
            cur_n -= count
        remaining_players[n] = cur_n
    return remaining_players

def func_2():
    t = int(input())
    results = []
    for _ in range(t):
        (k, q) = map(int, input().split())
        p = list(map(int, input().split()))
        qs = list(map(int, input().split()))
        remaining_players = func_1(p)
        res = [remaining_players[n] for n in qs]
        results.append(' '.join(map(str, res)))
    return results
output = func_2()
for result in output:
    print(result)