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
        
    #State: Output State: `results` is a list of integers where each integer represents the sum of counts of number pairs `(r_x, r_y)` for each input list `arr` in `test_cases`. Specifically, for each tuple `(n, x, y, arr)` in `test_cases`, the loop calculates how many times each pair of residues `(r_x, r_y)` appears, where `r_x = -num % x` and `r_y = num % y` for every `num` in `arr`, and then sums these counts to append to `results`.
    return results
    #The program returns a list of integers where each integer represents the sum of counts of number pairs (r_x, r_y) for each input list arr in test_cases.
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains three integers (n, x, y) followed by a list of n integers (a_1, a_2, ..., a_n). For each input list arr in the test_cases, it calculates the sum of counts of number pairs (r_x, r_y) for each element in arr, where r_x = -num % x and r_y = num % y. It then appends these sums to a results list and returns this list.

