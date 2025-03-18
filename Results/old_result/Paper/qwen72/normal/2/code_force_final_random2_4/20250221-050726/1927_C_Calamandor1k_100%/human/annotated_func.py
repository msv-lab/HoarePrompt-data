#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), and cases is a list of tuples, where each tuple contains three elements: n, m, and k (1 ≤ n, m ≤ 2·10^5, 2 ≤ k ≤ 2·min(n, m), and k is even), followed by two lists of integers a and b (1 ≤ a_i, b_j ≤ 10^6) of lengths n and m respectively.
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
        
    #State: `t` is a positive integer (1 ≤ t ≤ 10^4), `cases` is a list of tuples containing `t` tuples (n, m, k, a, b), `results` is a list containing 'YES' or 'NO' for each tuple in `cases` based on the conditions checked in the loop. For each tuple, `unique_a` is a set containing the unique elements from the list `a`, `unique_b` is a set containing the unique elements from the list `b`, `relevant_a` is a set containing elements from `unique_a` that are less than or equal to `k`, `relevant_b` is a set containing elements from `unique_b` that are less than or equal to `k`, `only_a` is a set containing elements that are in `relevant_a` but not in `relevant_b`, `only_b` is a set containing elements that are in `relevant_b` but not in `relevant_a`, `both` is a set containing elements that are in both `relevant_a` and `relevant_b`, and `total_distinct` is the sum of the lengths of `only_a`, `only_b`, and `both`.
    return results
    #The program returns a list `results` containing 'YES' or 'NO' for each tuple in `cases`. Each 'YES' or 'NO' indicates whether the conditions checked in the loop for the corresponding tuple (n, m, k, a, b) were met. The conditions involve checking the unique elements in lists `a` and `b` that are less than or equal to `k`, and ensuring the total number of distinct elements (those only in `a`, only in `b`, or in both) meets certain criteria.
#Overall this is what the function does:The function `func_1` takes a positive integer `t` and a list of tuples `cases` as input. Each tuple in `cases` consists of five elements: `n`, `m`, `k`, `a`, and `b`, where `n` and `m` are positive integers, `k` is an even integer, and `a` and `b` are lists of integers. The function evaluates each tuple to determine if the conditions related to the unique elements in `a` and `b` that are less than or equal to `k` are met. Specifically, it checks if the number of unique elements in `a` and `b` that are not shared and the number of shared elements together meet the criteria defined by `k`. The function returns a list `results` containing 'YES' or 'NO' for each tuple, indicating whether the conditions were met for that tuple.

