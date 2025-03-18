#State of the program right berfore the function call: The function is expected to handle multiple test cases. Each test case consists of an integer n (2 ≤ n ≤ 50) representing the number of cells in the ribbon, and a list of n integers (0 or 1) representing the state of each cell, where 0 indicates a free cell and 1 indicates a cell with a chip. At least one cell in each test case contains a chip.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: `t` is 0, `_` is a placeholder that has been incremented `t` times, `n` is the last input integer, `a` is the last list of integers with all leading and trailing zeros removed, `i` is the last index of the last list `a` (if `a` is not empty, otherwise `i` is undefined), and `res` is the number of zeros in the last list `a`.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` (2 ≤ n ≤ 50) representing the number of cells in a ribbon, and a list of `n` integers (0 or 1) representing the state of each cell, where 0 indicates a free cell and 1 indicates a cell with a chip. For each test case, the function removes all leading and trailing free cells (0s) from the list and then counts the number of remaining free cells (0s) in the list. The function prints the count of free cells for each test case. After processing all test cases, the function concludes without returning any value.

