#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains an integer n (2 ≤ n ≤ 2 · 10^5) representing the size of the array, two integers x and y (1 ≤ x, y ≤ 10^9) representing Polycarp's favorite integers, and a list a of n integers (1 ≤ a_i ≤ 10^9) representing the elements of the array. The total number of elements across all arrays in test_cases does not exceed 2 · 10^5.
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
        
    #State: `test_cases` is a list of tuples, where each tuple contains an integer n (2 ≤ n ≤ 2 · 10^5) representing the size of the array, two integers x and y (1 ≤ x, y ≤ 10^9) representing Polycarp's favorite integers, and a list a of n integers (1 ≤ a_i ≤ 10^9) representing the elements of the array. The total number of elements across all arrays in `test_cases` does not exceed 2 · 10^5; `results` is a list of integers, each representing the count of valid pairs for the corresponding test case in `test_cases`.
    return results
    #The program returns `results`, which is a list of integers. Each integer in this list represents the count of valid pairs for the corresponding test case in `test_cases`.
#Overall this is what the function does:The function `func_1` processes a list of test cases, where each test case consists of an integer `n`, two integers `x` and `y`, and a list `a` of `n` integers. It calculates the number of valid pairs in each test case based on specific residue conditions and returns a list of these counts.

