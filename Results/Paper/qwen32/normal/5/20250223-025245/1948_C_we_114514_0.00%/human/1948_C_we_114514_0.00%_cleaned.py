def func_1(t, test_cases):
    results = []
    for test_case in test_cases:
        (n, (row1, row2)) = test_case
        reachable_first_row = True
        reachable_second_row = False
        for j in range(n):
            if reachable_first_row:
                if row1[j] == '>':
                    if j == n - 1:
                        reachable_second_row = True
                else:
                    reachable_first_row = False
                    if j < n - 1 and row2[j] == '>':
                        reachable_second_row = True
            if reachable_second_row:
                if row2[j] == '>':
                    if j == n - 1:
                        reachable_second_row = True
        if reachable_second_row:
            results.append('YES')
        else:
            results.append('NO')
    return results
if __name__ == '__main__':
    t = int(input())
    test_cases = []
    for _ in range(t):
        n = int(input())
        row1 = input().strip()
        row2 = input().strip()
        test_cases.append((n, (row1, row2)))
    results = func_1(t, test_cases)
    for result in results:
        print(result)