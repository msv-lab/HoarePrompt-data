def func_1(t, cases):
    results = []
    for (n, m, k, a, b) in cases:
        unique_a = set(a)
        unique_b = set(b)
        relevant_a = {x for x in unique_a if x <= k}
        relevant_b = {x for x in unique_b if x <= k}
        only_a = relevant_a - relevant_b
        only_b = relevant_b - relevant_a
        both = relevant_a & relevant_b
        if len(only_a) > k // 2:
            results.append('NO')
            continue
        if len(only_b) > k // 2:
            results.append('NO')
            continue
        total_distinct = len(only_a) + len(only_b) + len(both)
        if total_distinct < k:
            results.append('NO')
            continue
        results.append('YES')
    return results
t = int(input())
cases = []
for _ in range(t):
    (n, m, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cases.append((n, m, k, a, b))
results = func_1(t, cases)
for result in results:
    print(result)