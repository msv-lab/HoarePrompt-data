#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers (n, x, y) and a list of n integers (a_1, a_2, ..., a_n). The integers n, x, and y satisfy 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9 for each a_i in the list. The total number of elements across all lists in test_cases does not exceed 2 * 10^5.
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
        
    #State: results
    return results
    #The program returns results
#Overall this is what the function does:The function `func_1` processes a list of test cases, where each test case consists of three integers (n, x, y) and a list of n integers. It calculates a count for each test case based on specific residue conditions and returns a list of these counts.

