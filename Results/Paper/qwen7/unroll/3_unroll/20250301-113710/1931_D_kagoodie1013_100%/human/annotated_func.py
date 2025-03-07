#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers (n, x, y) followed by a list of n integers (a_1, a_2, ..., a_n). The values of n, x, and y satisfy 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9 for all i. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1(test_cases):
    results = []
    for (n, x, y, arr) in test_cases:
        count = 0
        
        residue_map = {}
        
        for num in arr:
            r_x = -num % x
            r_y = num % y
            count += residue_map.get((r_x, r_y), 0)
            current_key = num % x, num % y
            residue_map[current_key] = residue_map.get(current_key, 0) + 1
        
        results.append(count)
        
    #State: Output State: `results` is a list of integers, where each integer represents the sum of counts of residue pairs `(r_x, r_y)` for each list of integers `arr` in `test_cases`. For each tuple `(n, x, y, arr)` in `test_cases`, the loop calculates the count of unique pairs of residues `(r_x, r_y)` for every number `num` in `arr`, where `r_x = -num % x` and `r_y = num % y`, and appends the total count to `results`.
    return results
    #The program returns a list of integers called 'results', where each integer represents the sum of counts of residue pairs (r_x, r_y) for each list of integers 'arr' in 'test_cases'. For each tuple (n, x, y, arr) in 'test_cases', the loop calculates the count of unique pairs of residues (r_x, r_y) for every number 'num' in 'arr', where r_x = -num % x and r_y = num % y, and appends the total count to 'results'.
#Overall this is what the function does:The function accepts a list of tuples `test_cases`, where each tuple contains three integers (n, x, y) followed by a list of n integers (a_1, a_2, ..., a_n). It calculates the sum of counts of residue pairs (r_x, r_y) for each list of integers `arr` in `test_cases`. For each number `num` in `arr`, it computes r_x = -num % x and r_y = num % y, and keeps track of these pairs using a dictionary `residue_map`. The function then appends the total count of unique pairs (r_x, r_y) for each list `arr` to the list `results`. Finally, it returns the list `results`, where each element represents the total count of such residue pairs for the corresponding list in `test_cases`.

