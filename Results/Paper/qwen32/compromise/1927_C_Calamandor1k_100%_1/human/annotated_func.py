#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case in the list 'cases' is a tuple containing three elements: (n, m, k) where n and m are integers such that 1 <= n, m <= 2*10^5, and k is an even integer such that 2 <= k <= 2 * min(n, m). The next two elements in each test case are lists 'a' and 'b' of lengths n and m respectively, where each element in 'a' and 'b' is an integer between 1 and 10^6 inclusive. The sum of all n and m across all test cases does not exceed 4 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; each test case in the list 'cases' is a tuple containing three elements: (n, m, k) where n and m are integers such that 1 <= n, m <= 2*10^5, and k is an even integer such that 2 <= k <= 2 * min(n, m); the next two elements in each test case are lists 'a' and 'b' of lengths n and m respectively, where each element in 'a' and 'b' is an integer between 1 and 10^6 inclusive; `results` is a list containing 'YES' or 'NO' for each test case in 'cases' based on the conditions specified in the loop.
    return results
    #The program returns `results`, which is a list containing 'YES' or 'NO' for each test case in `cases` based on the specified conditions.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, and lists `a` and `b` of lengths `n` and `m` respectively. For each test case, it determines if it's possible to select `k` distinct elements such that at most `k/2` elements are from list `a` and at most `k/2` elements are from list `b`. It returns a list of 'YES' or 'NO' indicating whether the condition is met for each test case.

