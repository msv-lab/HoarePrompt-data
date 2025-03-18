#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), and cases is a list of tuples where each tuple contains three integers n, m, and k (1 ≤ n, m ≤ 2·10^5, 2 ≤ k ≤ 2·min(n, m), and k is even), followed by two lists of integers a and b (1 ≤ a_i, b_j ≤ 10^6) representing the arrays a and b, respectively. The sum of values n and m over all test cases does not exceed 4·10^5.
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
        
    #State: `results` is a list of strings, each either 'YES' or 'NO', corresponding to whether the conditions in the loop are met for each tuple in `cases`. The length of `results` is equal to the length of `cases`.
    return results
    #The program returns a list of strings, `results`, where each string is either 'YES' or 'NO', indicating whether the conditions in the loop were met for each tuple in `cases`. The length of `results` is equal to the length of `cases`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list of tuples `cases`. Each tuple in `cases` contains three integers `n`, `m`, and `k`, and two lists of integers `a` and `b`. The function evaluates each tuple to determine if the conditions are met: specifically, it checks if the number of unique elements in `a` and `b` that are less than or equal to `k` and not shared between the two lists does not exceed `k // 2`, and if the total number of distinct elements in `a` and `b` that are less than or equal to `k` is at least `k`. The function returns a list of strings, `results`, where each string is either 'YES' or 'NO', indicating whether the conditions were met for each tuple. The length of `results` is equal to the number of tuples in `cases`.

