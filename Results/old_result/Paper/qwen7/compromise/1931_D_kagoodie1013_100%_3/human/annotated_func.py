#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers (n, x, y) representing the size of the array and Polycarp's favorite integers, followed by a list of n integers representing the elements of the array. The length of each tuple is n + 3, and it is guaranteed that 2 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, y ≤ 10^9, and 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: `results` is a list containing the final value of `count` after processing all arrays in `test_cases`. `residue_map` is a dictionary containing the count of each unique `(r_x, r_y)` pair across all arrays. `count` is the sum of all values obtained from `residue_map.get((r_x, r_y), 0)` for each `num` in all arrays. `current_key` is the last computed key `num % x, num % y` from the final iteration of the loop over all arrays. `r_x` is `-num % x` and `r_y` is `num % y` for each `num` in all arrays.
    return results
    #The program returns a list `results` containing the final value of `count` after processing all arrays in `test_cases`.
#Overall this is what the function does:The function accepts a list of tuples `test_cases`, where each tuple contains the size of the array `n`, and two integers `x` and `y`, followed by a list of `n` integers representing the elements of the array. It processes each array to count the number of pairs `(r_x, r_y)` where `r_x = -num % x` and `r_y = num % y` for each element `num` in the array. The function returns a list `results` containing the total count of such pairs for each array in `test_cases`.

