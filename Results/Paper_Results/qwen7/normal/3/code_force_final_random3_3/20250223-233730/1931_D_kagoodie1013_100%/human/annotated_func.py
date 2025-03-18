#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers \( n \), \( x \), and \( y \) followed by a list of \( n \) integers representing the array \( a \). The constraints are \( 1 \leq t \leq 10^4 \), \( 2 \leq n \leq 2 \cdot 10^5 \), \( 1 \leq x, y \leq 10^9 \), and \( 1 \leq a_i \leq 10^9 \). The sum of \( n \) over all test cases does not exceed \( 2 \cdot 10^5 \).
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
        
    #State: Output State: `results` is a list containing the cumulative sum of `count` values from all iterations, `count` is the total sum of occurrences of each unique pair `(r_x, r_y)` across all elements in all arrays in `test_cases`, `residue_map` is a dictionary that records the frequency of each unique pair `(r_x, r_y)` derived from all elements in all arrays in `test_cases`, `n` is the number of elements in the last test case array minus the number of elements processed so far, `x` is the third element of the last test case tuple, `y` is the third element of the last test case tuple, `arr` is the last test case array without the elements already processed, `num` is the current element being processed in the last array, `r_x` is the remainder of `-num % x`, `r_y` is the remainder of `num % y`, and `current_key` is the key `(num % x, num % y)` for the last element processed.
    #
    #In simpler terms, after the loop has executed all its iterations, `results` will contain the final count of occurrences of each unique `(r_x, r_y)` pair across all arrays in `test_cases`. The `residue_map` will show how many times each unique `(r_x, r_y)` pair appeared in the arrays. The remaining variables (`n`, `x`, `y`, `arr`, `num`, `r_x`, `r_y`, and `current_key`) will reflect the state just before the last element of the last array is processed.
    return results
    #The program returns a list named `results` that contains the cumulative sum of `count` values from all iterations. This list reflects the final count of occurrences of each unique `(r_x, r_y)` pair across all arrays in `test_cases`. Additionally, the `residue_map` dictionary shows how many times each unique `(r_x, r_y)` pair appeared in the arrays. The variables `n`, `x`, `y`, `arr`, `num`, `r_x`, `r_y`, and `current_key` reflect their state just before the last element of the last array is processed.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases` as input. Each tuple contains three integers \( n \), \( x \), and \( y \) followed by a list of \( n \) integers representing the array \( a \). It processes each test case to count the occurrences of each unique pair \((r_x, r_y)\), where \( r_x = -num \mod x \) and \( r_y = num \mod y \) for each element \( num \) in the array. The function accumulates these counts into a list `results`, which it returns. Additionally, it maintains a dictionary `residue_map` that records the frequency of each unique \((r_x, r_y)\) pair. After processing all test cases, the function returns the `results` list and the `residue_map` dictionary. The final states of the variables `n`, `x`, `y`, `arr`, `num`, `r_x`, `r_y`, and `current_key` reflect their state just before the last element of the last array is processed.

