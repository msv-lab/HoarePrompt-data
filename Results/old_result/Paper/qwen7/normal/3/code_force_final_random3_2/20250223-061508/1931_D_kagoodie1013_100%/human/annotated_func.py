#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers (n, x, y) followed by a list of n integers (a_1, a_2, ..., a_n). The value of n satisfies 2 <= n <= 2 * 10^5, and each x and y satisfies 1 <= x, y <= 10^9. Additionally, each a_i satisfies 1 <= a_i <= 10^9, and the sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `results` is a list of integers where each integer represents the total count of occurrences of each unique pair \((r_x, r_y)\) found across all arrays \(arr\) in `test_cases` according to the given conditions; `count` is the cumulative sum of these occurrences for each unique pair; `r_x` and `r_y` reflect the last computed values from the entire loop execution; `current_key` represents the last key computed; `residue_map` is a dictionary containing all unique \((r_x, r_y)\) pairs encountered during the loop, along with their frequencies; `num`, `x`, `y`, and `arr` are the last values from the final tuple in `test_cases`.
    return results
    #The program returns the list `results` which contains the total count of occurrences of each unique pair (r_x, r_y) found across all arrays arr in `test_cases` according to the given conditions.
#Overall this is what the function does:The function accepts a list of tuples `test_cases`, where each tuple contains three integers (n, x, y) followed by a list of n integers (a_1, a_2, ..., a_n). It calculates the total count of occurrences of each unique pair (r_x, r_y) for each array `arr` in `test_cases`, where r_x = -num % x and r_y = num % y for each number num in the array. The function returns a list `results` containing these counts for all arrays in `test_cases`.

