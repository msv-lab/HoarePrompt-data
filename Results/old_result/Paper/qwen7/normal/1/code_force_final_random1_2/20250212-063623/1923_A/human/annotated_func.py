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
        
    #State: Output State: `t` is greater than 0 and less than or equal to 1000, `n` is the integer input by the user for each iteration, `arr` is the input string with spaces removed for each iteration, `x` is the index of the first occurrence of '1' in `arr` or -1 if '1' is not found for each iteration, `y` is the index of the last occurrence of '1' in the reversed string `arr` or -1 if '1' is not found for each iteration, `z` is the substring from `arr` starting at index `x` and ending at index `n - y - 1` if `x` is not -1 and `n - y - 1` is within the bounds of `arr`, otherwise `z` remains unchanged for each iteration.
    #
    #This means that after all iterations of the loop have finished, `t` will be reduced to 0 because it starts as an input integer `t` and decreases by 1 in each iteration until it reaches 0. For each of the `t` inputs, the variables `n`, `arr`, `x`, `y`, and `z` will be set based on the specific input for that iteration. The final state will reflect the processing of all `t` inputs through the loop, with `t` being 0 and all other variables reflecting their last computed values from the respective iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (number of test cases), an integer n (number of cells), and a sequence of n binary values indicating whether each cell is free (0) or contains a chip (1). For each test case, it finds and counts the number of consecutive free cells between the first and last chip, printing the count of free cells. After processing all test cases, it outputs the counts for each case.

