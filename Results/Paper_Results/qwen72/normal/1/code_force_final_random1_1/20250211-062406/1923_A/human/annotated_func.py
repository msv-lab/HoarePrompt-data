#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, representing the number of test cases. For each test case, n is an integer such that 2 <= n <= 50, representing the number of cells. a is a list of n integers where each integer is either 0 or 1, representing whether a cell is free (0) or contains a chip (1), and at least one cell contains a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: After the loop executes all iterations, `t` is 0, `n` is the last input integer, `arr` is the last input string with all spaces removed, `x` is the index of the first occurrence of '1' in the last `arr`, or `-1` if '1' is not found in the last `arr`, `y` is the index of the last occurrence of '1' in the last `arr`, or `-1` if '1' is not found in the last `arr`, `z` is the substring of the last `arr` from index `x` to `n - y - 1` if `x` and `y` are valid and `n - y > x`, otherwise `z` is an empty string.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case consists of an integer `n` followed by a sequence of `n` integers (0s and 1s) representing the state of cells. The function calculates and prints the number of free cells (0s) between the first and last occupied cells (1s) for each test case. After processing all test cases, the function has no return value, and the final state of the program includes the last values of `t`, `n`, `arr`, `x`, `y`, and `z` as described in the annotations.

