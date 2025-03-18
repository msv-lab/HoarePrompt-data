#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, cases is a list of tuples, where each tuple contains three integers (n, m, k) representing the lengths of arrays a and b, and the number of elements to be chosen, respectively. Arrays a and b are represented as lists of integers, where 1 ≤ n, m ≤ 2⋅10^5 and 2 ≤ k ≤ 2⋅min(n, m), with k being even. Additionally, it is guaranteed that the sum of values n and m over all test cases in a test does not exceed 4⋅10^5.
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
        
    #State: Output State: The `results` list will contain either 'YES' or 'NO' for each test case based on the conditions specified in the loop. Specifically, for each test case (n, m, k, a, b):
    #
    #- If more than half of the elements in `only_a` or `only_b` exist (i.e., their counts exceed `k // 2`), the result for that test case will be 'NO'.
    #- If the total number of distinct elements in `only_a`, `only_b`, and `both` is less than `k`, the result for that test case will also be 'NO'.
    #- Otherwise, the result for that test case will be 'YES'.
    #
    #All other variables (`unique_a`, `unique_b`, `relevant_a`, `relevant_b`, `both`, `only_a`, `only_b`) will be recalculated for each test case but will not persist outside the current iteration. The final `results` list will include the outcome ('YES' or 'NO') for every test case processed by the loop.
    #
    #In summary, the `results` list will contain the outcome for each test case after all iterations of the loop have completed, with no additional variables persisting beyond their scope within the loop.
    return results
    #The program returns a list of strings, either 'YES' or 'NO', for each test case processed by the loop. Each entry in the list is determined based on whether more than half of the elements in `only_a` or `only_b` exist (i.e., their counts exceed `k // 2`), or if the total number of distinct elements in `only_a`, `only_b`, and `both` is less than `k`. If neither condition is met, the entry is 'YES'.
#Overall this is what the function does:The function processes a list of test cases, each containing the lengths of two arrays (a and b) and the number of elements to choose (k). For each test case, it determines if the chosen elements meet specific criteria. If more than half of the elements in either array a or b exceed k/2, or if the total number of distinct elements is less than k, the result is 'NO'. Otherwise, the result is 'YES'. The function returns a list of these results, one for each test case.

