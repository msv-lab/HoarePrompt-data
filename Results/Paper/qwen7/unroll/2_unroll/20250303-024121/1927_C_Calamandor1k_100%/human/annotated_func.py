#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, cases is a list of tuples, where each tuple contains three integers n, m, and k such that 1 ≤ n, m ≤ 2⋅10^5, 2 ≤ k ≤ 2⋅min(n, m), and k is even. Additionally, for each test case, there are n integers in the second element of the tuple representing array a, and m integers in the third element of the tuple representing array b, with each element of arrays a and b being an integer between 1 and 10^6 inclusive. The sum of values n and m over all test cases does not exceed 4⋅10^5.
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
        
    #State: Output State: `results` is a list that contains either 'YES' or 'NO' for each test case based on the conditions specified in the loop. If for any test case, the number of elements in `only_a` or `only_b` exceeds `k // 2`, or the total number of distinct elements in `only_a`, `only_b`, and `both` is less than `k`, then 'NO' is appended to the `results` list for that test case. Otherwise, 'YES' is appended.
    return results
    #The program returns a list 'results' that contains either 'YES' or 'NO' for each test case based on the conditions specified in the loop. For each test case, if the number of elements in 'only_a' or 'only_b' exceeds k // 2, or the total number of distinct elements in 'only_a', 'only_b', and 'both' is less than k, then 'NO' is appended to the 'results' list for that test case. Otherwise, 'YES' is appended.
#Overall this is what the function does:The function `func_1` takes two parameters: `t`, a positive integer between 1 and 10^4, and `cases`, a list of tuples. Each tuple contains three integers `n`, `m`, and `k` with specific constraints, and two lists `a` and `b`. For each test case, the function processes `a` and `b` to find unique elements within the range up to `k`, identifies elements exclusive to `a` or `b`, and those common to both. It then checks if the number of exclusive elements in `a` or `b` exceeds `k // 2`, or if the total number of distinct elements is less than `k`. If any of these conditions are met, it appends 'NO' to the results list; otherwise, it appends 'YES'. The function returns a list of 'YES' or 'NO' for each test case based on these conditions.

