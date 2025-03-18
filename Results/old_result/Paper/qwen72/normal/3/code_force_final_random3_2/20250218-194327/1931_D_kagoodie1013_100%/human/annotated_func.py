#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three elements: n, x, and y, such that 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and a list of integers a of length n, such that 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `test_cases` is a list of tuples, `n` is the first element of the last tuple processed, `x` is the second element of the last tuple processed, `y` is the third element of the last tuple processed, `arr` is the fourth element of the last tuple processed and has `len(arr)` elements, `results` is a list containing the final `count` value for each tuple in `test_cases`, `count` is the total number of pairs `(r_x, r_y)` that have been encountered more than once for the last tuple processed, `residue_map` contains keys that are tuples of the form `(num % x, num % y)` for each `num` in the last `arr`, and the value for each key is the number of times that pair has been encountered, `num` is the last element of the last `arr` processed, `r_x` is `-num % x` for the last element, `r_y` is `num % y` for the last element, `current_key` is a tuple containing the values of `num % x` and `num % y` for the last element.
    return results
    #The program returns the list `results` which contains the final `count` value for each tuple in `test_cases`. The `count` value for each tuple represents the total number of pairs `(r_x, r_y)` that have been encountered more than once for that tuple, where `r_x` is `-num % x` and `r_y` is `num % y` for each `num` in the `arr` of that tuple.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases`, where each tuple contains four elements: an integer `n`, integers `x` and `y`, and a list of integers `arr` of length `n`. It processes each tuple to count the number of pairs `(r_x, r_y)` that have been encountered more than once, where `r_x` is `-num % x` and `r_y` is `num % y` for each `num` in `arr`. The function returns a list `results` where each element corresponds to the count of such pairs for each tuple in `test_cases`. After the function concludes, `test_cases` remains unchanged, and `results` contains the final counts for each tuple.

