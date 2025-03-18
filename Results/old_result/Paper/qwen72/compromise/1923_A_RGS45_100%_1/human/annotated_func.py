#State of the program right berfore the function call: The function is expected to handle multiple test cases. Each test case consists of an integer n (2 ≤ n ≤ 50) representing the number of cells in the ribbon, and a list of n integers (0 or 1) representing the state of each cell, where 0 indicates a free cell and 1 indicates a cell containing a chip. At least one cell in each test case contains a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The loop will execute `t` times, and for each iteration, it will print the number of free cells (0s) between the first and last chip (1s) in the ribbon. The variables `n`, `arr`, `x`, `y`, and `z` will be updated for each test case, but the value of `t` will remain unchanged. After all iterations, the loop will have completed its execution, and the final state of `t` will be the same as the initial state.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` (2 ≤ n ≤ 50) and a list of `n` integers (0 or 1) representing the state of a ribbon, where 0 indicates a free cell and 1 indicates a cell containing a chip. The function then prints the number of free cells (0s) between the first and last chip (1s) in the ribbon for each test case. The function does not return any value; it only prints the results. After all test cases are processed, the function completes its execution, and the state of the program is such that all test cases have been handled and the corresponding counts of free cells have been printed.

