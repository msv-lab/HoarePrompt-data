#State of the program right berfore the function call: test_cases is a list of test case descriptions. Each test case description is a tuple containing three integers (n, x, y) and a list of n integers (a). Here, n is the size of the array (2 <= n <= 2 * 10^5), x and y are Polycarp's favorite integers (1 <= x, y <= 10^9), and a is the list of integers (1 <= a_i <= 10^9). The length of the test_cases list is t (1 <= t <= 10^4), and the sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `test_cases` is a list of test case descriptions that has been fully iterated over; `results` is a list containing the final value of `count` for each test case in `test_cases`; `count` is not defined outside the loop as it is local to each iteration; `n`, `x`, `y`, and `arr` are the values from the last test case processed with `arr` fully processed; `residue_map` is a dictionary containing the frequency of each pair `(num % x, num % y)` encountered in the last `arr`.
    return results
    #The program returns `results`, which is a list containing the final value of `count` for each test case in `test_cases`.
#Overall this is what the function does:The function processes a list of test cases, where each test case consists of integers \( n \), \( x \), \( y \), and a list of \( n \) integers \( a \). For each test case, it calculates a count based on specific residue conditions related to \( x \) and \( y \) and the elements in \( a \). The function returns a list of these counts, one for each test case.

