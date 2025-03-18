#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, cases is a list of tuples, where each tuple contains three integers (n, m, k) representing the lengths of arrays a and b, and the number of elements to be chosen, respectively. Additionally, n, m, and k satisfy 1 ≤ n, m ≤ 2⋅10^5, 2 ≤ k ≤ 2⋅min(n, m), and k is even. Arrays a and b are represented as lists of integers, where each element in a and b satisfies 1 ≤ a_i, b_j ≤ 10^6. It is guaranteed that the sum of values n and m over all test cases in a test does not exceed 4⋅10^5.
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
        
    #State: The `results` list contains either 'YES' or 'NO' for each iteration of the loop, based on the conditions specified in the loop body. The length of the `results` list is equal to the number of test cases in the `cases` list.
    return results
    #The program returns a list named 'results' which contains either 'YES' or 'NO' for each iteration of the loop, based on the conditions specified in the loop body. The length of the 'results' list is equal to the number of test cases in the 'cases' list.
#Overall this is what the function does:The function `func_1` takes two parameters: `t`, a positive integer between 1 and 10^4, and `cases`, a list of tuples. Each tuple contains three integers (n, m, k) representing the lengths of arrays `a` and `b`, and the number of elements to be chosen, respectively. The function processes each test case in the `cases` list, checks specific conditions related to the elements in arrays `a` and `b`, and appends either 'YES' or 'NO' to the `results` list based on these conditions. The function returns the `results` list, which contains the outcome ('YES' or 'NO') for each test case.

