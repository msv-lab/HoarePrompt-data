#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), and cases is a list of tuples, where each tuple contains three elements: n, m, and k. For each tuple, n and m are positive integers (1 ≤ n, m ≤ 2·10^5), and k is an even integer (2 ≤ k ≤ 2·min(n, m)). Each test case is followed by two lists of integers, a and b, with lengths n and m, respectively, and each element in a and b is an integer (1 ≤ a_i, b_j ≤ 10^6).
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
        
    #State: The `results` list is populated with 'YES' or 'NO' for each tuple in `cases` based on the conditions checked in the loop. The `cases` list remains unchanged.
    return results
    #The program returns the `results` list, which is populated with 'YES' or 'NO' for each tuple in the `cases` list based on the conditions checked in the loop. The `cases` list remains unchanged.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list of tuples `cases`. Each tuple in `cases` contains five elements: `n`, `m`, `k`, `a`, and `b`, where `n` and `m` are positive integers, `k` is an even integer, and `a` and `b` are lists of integers. The function returns a list `results` where each element is 'YES' or 'NO' based on whether the conditions for each tuple in `cases` are met. Specifically, 'YES' is appended to `results` if the number of elements in `a` that are not in `b` and the number of elements in `b` that are not in `a` are both less than or equal to `k // 2`, and the total number of distinct elements in `a` and `b` that are less than or equal to `k` is at least `k`. Otherwise, 'NO' is appended. The `cases` list remains unchanged.

