#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case in cases is a tuple (n, m, k, a, b) where n and m are integers such that 1 <= n, m <= 2*10^5, k is an even integer such that 2 <= k <= 2*min(n, m), a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, and b is a list of m integers where each integer b_j satisfies 1 <= b_j <= 10^6. The sum of all n and m across all test cases does not exceed 4*10^5.
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
        
    #State: `results` is a list containing 'YES' or 'NO' for each test case in `cases` based on the conditions specified in the loop. `t` remains unchanged. `cases` remains unchanged.
    return results
    #The program returns the list `results` which contains 'YES' or 'NO' for each test case in `cases` based on the conditions specified in the loop.
#Overall this is what the function does:The function `func_1` takes an integer `t` representing the number of test cases and a list `cases` containing `t` tuples. Each tuple consists of integers `n`, `m`, `k`, a list `a` of `n` integers, and a list `b` of `m` integers. It evaluates each test case based on specific conditions and returns a list `results` containing 'YES' or 'NO' for each test case. The function does not modify the input parameters `t` or `cases`.

