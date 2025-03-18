#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case is described by three integers n, m, and k where 1 ≤ n, m ≤ 2·10^5, 2 ≤ k ≤ 2·min(n, m), and k is even. a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6. b is a list of m integers where each integer b_j satisfies 1 ≤ b_j ≤ 10^6. The sum of all n and m over all test cases does not exceed 4·10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4. Each test case is described by three integers n, m, and k where 1 ≤ n, m ≤ 2·10^5, 2 ≤ k ≤ 2·min(n, m), and k is even. `a` is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6. `b` is a list of m integers where each integer b_j satisfies 1 ≤ b_j ≤ 10^6. The sum of all n and m over all test cases does not exceed 4·10^5. `results` is a list containing 'YES' or 'NO' for each test case based on the conditions specified in the loop.
    return results
    #The program returns a list `results` containing 'YES' or 'NO' for each test case based on the conditions specified in the loop.
#Overall this is what the function does:The function `func_1` processes a series of test cases, each defined by integers `n`, `m`, and `k`, and two lists of integers `a` and `b`. For each test case, it evaluates whether certain conditions related to the elements in `a` and `b` and the value of `k` are satisfied. It returns a list of 'YES' or 'NO' responses, one for each test case, indicating whether the conditions are met.

