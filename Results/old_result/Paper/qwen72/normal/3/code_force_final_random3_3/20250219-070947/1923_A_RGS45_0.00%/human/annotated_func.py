#State of the program right berfore the function call: The function is expected to handle multiple test cases. Each test case consists of an integer n (2 ≤ n ≤ 50) representing the number of cells in the ribbon, and a list of n integers (0 or 1) representing the state of each cell, where 0 indicates a free cell and 1 indicates a cell containing a chip. At least one cell in each test case contains a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The loop has executed `t` times, `_` is `t - 1`, `n` is the last input integer, `arr` is the last input string, `x` is the index of the first occurrence of '1' in the last `arr` or -1 if '1' is not found, `y` is the index of the first occurrence of '1' in the reversed last `arr` or -1 if '1' is not found, `z` is the substring of the last `arr` from index `x` to index `n - y - 1`.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of an integer `n` (2 ≤ n ≤ 50) and a string `arr` of length `n` containing '0's and '1's, where '1' represents a cell with a chip and '0' represents a free cell. For each test case, the function finds the first and last occurrence of '1' in the string `arr`, extracts the substring between these occurrences, and prints the count of '0's in this substring. After processing all test cases, the function has no return value, but it has printed the count of '0's for each test case.

