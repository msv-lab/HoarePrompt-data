#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers (n, x, y) and a list of n integers a, representing the size of the array, Polycarp's favorite integers, and the elements of the array, respectively. The constraints are 1 <= len(test_cases) <= 10^4, 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9 for each element a_i in the lists a. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1(test_cases):
    results = []
    for (n, x, y, arr) in test_cases:
        count = 0
        
        mod_x_map = {}
        
        mod_y_map = {}
        
        for num in arr:
            mod_x = -num % x
            mod_y = num % y
            count += mod_x_map.get(mod_x, 0) + mod_y_map.get(mod_y, 0)
            mod_x_key = num % x
            mod_y_key = num % y
            mod_x_map[mod_x_key] = mod_x_map.get(mod_x_key, 0) + 1
            mod_y_map[mod_y_key] = mod_y_map.get(mod_y_key, 0) + 1
        
        results.append(count)
        
    #State: `results` is a list where each element is the count of pairs (i, j) for each test case in `test_cases` such that `-arr[i] % x == arr[j] % x` or `arr[i] % y == arr[j] % y` for i < j. The state of `test_cases` remains unchanged.
    return results
    #The program returns the list `results`, where each element is the count of pairs (i, j) for each test case in `test_cases` such that `-arr[i] % x == arr[j] % x` or `arr[i] % y == arr[j] % y` for i < j.
#Overall this is what the function does:The function takes a list of test cases, where each test case consists of integers `n`, `x`, `y`, and a list of `n` integers `a`. It returns a list where each element represents the count of pairs `(i, j)` in the corresponding test case such that `-arr[i] % x == arr[j] % x` or `arr[i] % y == arr[j] % y` for `i < j`.

