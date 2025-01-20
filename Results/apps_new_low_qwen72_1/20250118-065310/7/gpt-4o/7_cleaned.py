def func_1(t, queries):
    results = []
    for query in queries:
        (n, x) = query[0]
        blows = query[1:]
        max_single_blow = 0
        max_effective_blow = float('-inf')
        for (d, h) in blows:
            if d >= x:
                results.append(1)
                break
            max_single_blow = max(max_single_blow, d)
            if d > h:
                max_effective_blow = max(max_effective_blow, d - h)
        else:
            if max_effective_blow <= 0:
                results.append(-1)
            else:
                remaining_heads = x - max_single_blow
                additional_blows = (remaining_heads + max_effective_blow - 1) // max_effective_blow
                results.append(additional_blows + 1)
    return results
input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
queries = []
for _ in range(t):
    (n, x) = (int(data[index]), int(data[index + 1]))
    index += 2
    blows = []
    for _ in range(n):
        (d, h) = (int(data[index]), int(data[index + 1]))
        blows.append((d, h))
        index += 2
    queries.append(((n, x), blows))
results = func_1(t, queries)
for result in results:
    print(result)