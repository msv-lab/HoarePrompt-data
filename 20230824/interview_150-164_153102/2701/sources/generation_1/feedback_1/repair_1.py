def minimum_time(N, K, apples):
    types = {}
    for i, t in enumerate(apples):
        if t not in types:
            types[t] = [i]
        else:
            types[t].append(i)
    for t in types:
        if K - t != t and K - t in types:
            return min(types[t]) + min(types[K - t]) + 2
    if len(types) == 2 and sum(types) == K:
        return sum(min(types.values()))
    if K % 2 == 0 and K / 2 in types:
        return 2 * min(types[K / 2])
    return -1

N, K = map(int, input().split())
apples = list(map(int, input().split()))
print(minimum_time(N, K, apples))