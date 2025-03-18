#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three elements: n (an integer such that 2 ≤ n ≤ 2 · 10^5), x (an integer such that 1 ≤ x ≤ 10^9), and y (an integer such that 1 ≤ y ≤ 10^9). Additionally, each test case is followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `results` is a list containing the count of pairs (i, j) for each test case, where 1 ≤ i < j ≤ n and (a_i + a_j) is divisible by both x and y. The `test_cases` list remains unchanged.
    return results
    #The program returns the list `results` which contains the count of pairs (i, j) for each test case, where 1 ≤ i < j ≤ n and (a_i + a_j) is divisible by both x and y. The list `test_cases` remains unchanged.
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case consists of a tuple with three integers (n, x, y) and a list of n integers. It returns a list of integers, where each integer represents the count of pairs (i, j) in the corresponding test case such that 1 ≤ i < j ≤ n and the sum (a_i + a_j) is divisible by both x and y. The input list `test_cases` remains unchanged.

