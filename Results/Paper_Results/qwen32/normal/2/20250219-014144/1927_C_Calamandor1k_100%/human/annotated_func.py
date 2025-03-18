#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case in the list 'cases' is a tuple containing three parts: (1) a tuple (n, m, k) where n and m are integers such that 1 ≤ n, m ≤ 2·10^5 and k is an even integer such that 2 ≤ k ≤ 2·min(n, m); (2) a list a of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6; (3) a list b of m integers where each integer b_j satisfies 1 ≤ b_j ≤ 10^6. The sum of all n and m across all test cases does not exceed 4·10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `cases` is a list containing `t` tuples (n, m, k, a, b) where n and m are integers such that 1 ≤ n, m ≤ 2·10^5, k is an even integer such that 2 ≤ k ≤ 2·min(n, m), a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6, b is a list of m integers where each integer b_j satisfies 1 ≤ b_j ≤ 10^6. `results` is a list containing `t` strings, each either `'YES'` or `'NO'`, determined by the conditions specified in the loop.
    return results
    #The program returns a list `results` containing `t` strings, each either `'YES'` or `'NO'`, determined by the conditions specified in the loop.
#Overall this is what the function does:The function takes an integer `t` representing the number of test cases and a list `cases` containing `t` tuples. Each tuple includes integers `n` and `m` indicating the lengths of two lists, an even integer `k`, and two lists `a` and `b` of lengths `n` and `m` respectively. For each test case, the function evaluates whether certain conditions related to the elements of lists `a` and `b` and the value of `k` are met. It returns a list of `t` strings, each either `'YES'` or `'NO'`, based on these evaluations.

