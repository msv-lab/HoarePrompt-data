#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers n, m, and k where 1 ≤ n, m ≤ 2·10^5, 2 ≤ k ≤ 2·min(n, m), and k is even. Additionally, each test case includes two lists: a list a of n integers where 1 ≤ a_i ≤ 10^6 for each i, and a list b of m integers where 1 ≤ b_j ≤ 10^6 for each j. The sum of all n and m across all test cases does not exceed 4·10^5.
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
        
    #State: ['YES', 'NO', 'YES']
    return results
    #The program returns results which is ['YES', 'NO', 'YES']
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of two lists of integers and some constraints. It determines whether it is possible to select `k` distinct integers from the union of these two lists under specific conditions and returns a list of 'YES' or 'NO' for each test case indicating the feasibility.

