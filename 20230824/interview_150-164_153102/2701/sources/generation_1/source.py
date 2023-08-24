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
    return -1

N, K = map(int, input().split())
apples = list(map(int, input().split()))
print(minimum_time(N, K, apples))