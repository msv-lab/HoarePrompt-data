#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. cases is a list of tuples, where each tuple contains three elements: n, m, and k (1 ≤ n, m ≤ 2·10^5, 2 ≤ k ≤ 2·min(n, m), and k is even), followed by two lists of integers a and b (1 ≤ a_i, b_j ≤ 10^6) of lengths n and m respectively. The sum of values n and m over all test cases does not exceed 4·10^5.
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
        
    #State: After all iterations of the loop have executed, `t` remains a positive integer (1 ≤ t ≤ 10^4), `cases` is an empty list, and `results` is a list containing either 'YES' or 'NO' for each tuple in the original `cases` list. For each tuple `(n, m, k, a, b)` processed by the loop, the following conditions were checked:
    return results
    #The program returns a list named 'results' which contains either 'YES' or 'NO' for each tuple that was originally in the `cases` list. The length of the `results` list is equal to the number of tuples that were processed, and each element corresponds to whether the conditions for the respective tuple were met ('YES') or not ('NO').
#Overall this is what the function does:The function `func_1` takes a positive integer `t` and a list of tuples `cases` as inputs. Each tuple in `cases` consists of five elements: `n`, `m`, `k`, `a`, and `b`. Here, `n` and `m` are positive integers, `k` is an even integer, and `a` and `b` are lists of integers. The function processes each tuple to determine if certain conditions are met, specifically checking the distinct elements in `a` and `b` that are less than or equal to `k`. It returns a list `results` containing 'YES' or 'NO' for each tuple, indicating whether the conditions were met ('YES') or not ('NO'). The length of the `results` list is equal to the number of tuples in `cases`. The original `cases` list remains unchanged.

