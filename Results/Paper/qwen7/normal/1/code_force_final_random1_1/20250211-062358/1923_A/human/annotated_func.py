#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 2 ≤ n ≤ 50; the second line of each test case contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1, indicating whether the i-th cell is free (0) or contains a chip (1); in each test case, at least one cell contains a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: Output State: `t` must be a positive integer, `n` is an input integer for each iteration, `arr` is the input string without spaces for each iteration, `x` is the index of the first occurrence of '1' in `arr` (if '1' is not found, `x` remains -1) for each iteration, `y` is the index of the last occurrence of '1' in `arr` (if '1' is not found, `y` remains -1) for each iteration, `z` is the substring of `arr` starting from index `x` and ending at index `n - y - 1` for each iteration, and the final result is the count of '0's in `z` for each iteration.
    #
    #This means that after all iterations of the loop have finished, `t` will be the total number of iterations, each iteration will have its own `n`, `arr`, `x`, `y`, and `z` based on user inputs, and the output will be the count of '0's in `z` for each iteration. The final output will be a series of counts of '0's from each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (number of test cases), an integer `n` (length of the binary string), and a binary string `arr` representing cells (0 for free, 1 for containing a chip). For each test case, it finds the first and last positions of '1' in `arr`, extracts the substring between these positions, and counts the number of '0's in this substring. The function outputs the count of '0's for each test case.

