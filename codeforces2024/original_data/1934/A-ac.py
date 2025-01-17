def max_expression(t, test_cases):
    results = []
    for n, array in test_cases:
        array.sort()
        candidates = [
            (array[0], array[1], array[-1], array[-2]),
            (array[0], array[-1], array[1], array[-2])
        ]
        max_val = 0
        for i, j, k, l in candidates:
            value = abs(i - j) + abs(j - k) + abs(k - l) + abs(l - i)
            max_val = max(max_val, value)
        results.append(max_val)
    return results
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    test_cases.append((n, array))
results = max_expression(t, test_cases)
for result in results:
    print(result)
