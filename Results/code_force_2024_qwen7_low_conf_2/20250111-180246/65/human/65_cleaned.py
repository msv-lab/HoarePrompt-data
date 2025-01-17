def func_1(test_cases):
    results = []
    for (p1, p2, p3) in test_cases:
        total_points = p1 + p2 + p3
        if total_points % 2 != 0 or p3 > p1 + p2:
            results.append(-1)
            continue
        max_draws = min(p1, p3 - p2) + min(p2, p3 - p1)
        results.append(max_draws)
    return results
if __name__ == '__main__':
    t = int(input())
    test_cases = []
    for _ in range(t):
        (p1, p2, p3) = map(int, input().split())
        test_cases.append((p1, p2, p3))
    results = func_1(test_cases)
    for result in results:
        print(result)