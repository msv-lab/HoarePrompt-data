#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, cases is a list of tuples, where each tuple contains three integers n, m, and k such that 1 ≤ n, m ≤ 2⋅10^5, 2 ≤ k ≤ 2⋅min(n, m), and k is even. Additionally, for each test case, there are n integers in the second list of the tuple representing array a, and m integers in the third list of the tuple representing array b, where 1 ≤ a_i, b_j ≤ 10^6. It is guaranteed that the sum of values n and m over all test cases in a test does not exceed 4⋅10^5.
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
        
    #State: Output State: `results` is a list that may contain 'YES' or 'NO' based on the conditions met during each iteration of the loop. Specifically, for each tuple (n, m, k, a, b) in `cases`, if the conditions regarding the sets `only_a`, `only_b`, and `both` are satisfied, 'YES' is appended to `results`; otherwise, 'NO' is appended. The exact contents of `results` depend on the values of `cases`.
    return results
    #`results` is a list containing 'YES' or 'NO' based on the conditions met during each iteration of the loop. For each tuple (n, m, k, a, b) in `cases`, if the conditions regarding the sets `only_a`, `only_b`, and `both` are satisfied, 'YES' is appended to `results`; otherwise, 'NO' is appended.
#Overall this is what the function does:The function `func_1` takes two parameters: `t`, a positive integer between 1 and 10^4, and `cases`, a list of tuples. Each tuple contains five elements: `n`, `m`, and `k` (all integers), and two lists `a` and `b`. For each tuple in `cases`, the function checks specific conditions involving sets derived from `a` and `b`. If these conditions are met, it appends 'YES' to the results list; otherwise, it appends 'NO'. The function returns the results list containing 'YES' or 'NO' for each tuple in `cases`.

