#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and cases is a list of tuples, where each tuple contains three elements: n, m, and k, and two lists a and b. For each tuple, n and m are integers such that 1 ≤ n, m ≤ 2·10^5, k is an even integer such that 2 ≤ k ≤ 2·min(n, m), and a and b are lists of integers of lengths n and m, respectively, with elements in the range 1 ≤ a_i, b_j ≤ 10^6. The sum of values n and m over all test cases does not exceed 4·10^5.
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
        
    #State: `results` is a list containing 'YES' or 'NO' for each tuple in `cases`, based on the conditions evaluated in the loop.
    return results
    #The program returns the list `results` which contains 'YES' or 'NO' for each tuple in `cases`, based on the conditions evaluated in the loop.
#Overall this is what the function does:The function `func_1` accepts an integer `t` and a list of tuples `cases`. Each tuple in `cases` contains integers `n`, `m`, and `k`, and two lists of integers `a` and `b`. The function evaluates each tuple to determine if the conditions are met for a specific problem, and returns a list `results` where each element is 'YES' or 'NO'. A 'YES' indicates that the conditions are met, and a 'NO' indicates that they are not. The conditions are: the number of unique elements in `a` that are not in `b` and are less than or equal to `k` should not exceed `k // 2`, the number of unique elements in `b` that are not in `a` and are less than or equal to `k` should not exceed `k // 2`, and the total number of distinct elements in both `a` and `b` that are less than or equal to `k` should be at least `k`.

