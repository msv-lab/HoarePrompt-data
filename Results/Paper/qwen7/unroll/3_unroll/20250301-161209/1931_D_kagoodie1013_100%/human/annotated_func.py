#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer such that 2 <= n <= 2 * 10^5), x and y (integers such that 1 <= x, y <= 10^9), and a list of n integers a (such that 1 <= a_i <= 10^9). The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: Output State: `results` is a list of integers where each integer represents the value of `count` calculated for each corresponding test case in `test_cases`. For each test case, `count` is determined by iterating through the list `arr`, calculating the residues of each element with respect to `x` and `y`, and counting the number of pairs of residues `(r_x, r_y)` that have been seen before.
    return results
    #The program returns a list of integers named `results` where each integer represents the count of unique residue pairs (r_x, r_y) for each corresponding test case in `test_cases`. Each test case involves iterating through the list `arr`, calculating the residues of each element with respect to `x` and `y`, and counting the number of such unique pairs encountered.
#Overall this is what the function does:The function `func_1` takes a list of tuples `test_cases` as input. Each tuple contains an integer `n`, two integers `x` and `y`, and a list of `n` integers `arr`. It processes each test case by iterating through the list `arr` and calculating the residues of each element with respect to `x` and `y`. It then counts the number of unique pairs of these residues and appends this count to a list `results`. Finally, it returns the list `results`, where each element represents the count of unique residue pairs `(r_x, r_y)` for each corresponding test case.

