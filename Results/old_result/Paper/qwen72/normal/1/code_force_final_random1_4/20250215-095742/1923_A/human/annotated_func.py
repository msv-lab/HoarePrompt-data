#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 50, representing the number of cells in the ribbon. a is a list of n integers where each integer a_i is either 0 or 1, representing whether the i-th cell is free (0) or contains a chip (1). At least one cell in each test case contains a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: After all iterations, `t` is 0, and for each test case, `n` was an input integer, `arr` was the input string with all spaces removed, `x` was the index of the first occurrence of '1' in `arr`, `y` was the index of the last occurrence of '1' in `arr`, and `z` was the substring of `arr` from index `x` to index `n - y - 1`. The loop printed the count of '0's in `z` for each test case.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case involves reading an integer `n` and a list of `n` integers (0s and 1s) representing the state of a ribbon. The function then calculates and prints the number of free cells (0s) between the first and last chip (1s) in the ribbon for each test case. After processing all test cases, the function completes its execution.

