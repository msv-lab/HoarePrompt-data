#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. Each element in cases is a tuple containing three elements: n, m, and k (1 ≤ n, m ≤ 2·10^5, 2 ≤ k ≤ 2·min(n, m), and k is even), followed by two lists of integers a and b (1 ≤ a_i, b_j ≤ 10^6) of lengths n and m, respectively. The sum of values n and m over all test cases does not exceed 4·10^5.
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
        
    #State: `t` is a positive integer (1 ≤ t ≤ 10^4), `cases` is a list of tuples where each tuple contains valid `n`, `m`, `k`, `a`, and `b` as described, and `cases` has been fully iterated through, `results` is a list containing the strings 'NO' or 'YES' for each test case in `cases`. For each test case, `unique_a` is a set containing the unique elements from the list `a`, `unique_b` is a set containing the unique elements from the list `b`, `relevant_a` is a set containing elements from `unique_a` that are less than or equal to `k`, `relevant_b` is a set containing elements from `unique_b` that are less than or equal to `k`, `only_a` is a set containing elements from `relevant_a` that are not in `relevant_b`, `only_b` is a set containing elements from `relevant_b` that are not in `relevant_a`, `both` is a set containing elements that are in both `relevant_a` and `relevant_b`, `total_distinct` is the sum of the lengths of `only_a`, `only_b`, and `both`. The final `results` list contains 'YES' if the conditions for each test case are met, otherwise it contains 'NO'.
    return results
    #The program returns a list `results` containing 'YES' or 'NO' for each test case in `cases`. Each 'YES' indicates that the conditions for the corresponding test case are met, while each 'NO' indicates that they are not. The conditions involve checking the uniqueness and overlap of elements in lists `a` and `b` relative to the value `k`.
#Overall this is what the function does:The function `func_1` takes a positive integer `t` and a list of test cases `cases`. Each test case is a tuple containing three integers `n`, `m`, and `k`, and two lists of integers `a` and `b`. The function evaluates each test case to determine if the conditions involving the uniqueness and overlap of elements in `a` and `b` relative to `k` are met. Specifically, it checks if the number of unique elements in `a` and `b` that are less than or equal to `k` and do not overlap exceeds `k // 2`, and if the total number of distinct elements (including those that overlap) is at least `k`. If these conditions are met, the function appends 'YES' to the results list; otherwise, it appends 'NO'. The function returns a list `results` containing 'YES' or 'NO' for each test case, indicating whether the conditions are met.

