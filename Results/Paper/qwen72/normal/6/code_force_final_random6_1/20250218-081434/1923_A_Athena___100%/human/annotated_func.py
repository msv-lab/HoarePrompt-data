#State of the program right berfore the function call: The function `func` is expected to be called within a context where it processes multiple test cases. Each test case includes an integer `n` (2 ≤ n ≤ 50) representing the number of cells in the ribbon, and a list `a` of length `n` containing integers (0 or 1) where 0 represents a free cell and 1 represents a cell with a chip. The input is provided in a structured format where the first line contains the number of test cases `t` (1 ≤ t ≤ 1000), followed by `t` test cases, each with two lines as described. In each test case, at least one cell contains a chip.
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
        
    #State: `t` is 0, all test cases have been processed, `n` and `a` are the last values read from input, `res` is the number of zeros in the last processed list `a` after removing leading and trailing zeros.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` and a list `a` of length `n` containing integers (0 or 1). For each test case, it calculates and prints the number of free cells (0s) that are not at the beginning or end of the list after removing any leading and trailing free cells. The function does not return any values; it only prints the results for each test case. After processing all test cases, the function concludes with `t` being 0, `n` and `a` holding the values from the last test case, and `res` being the number of free cells in the last processed list `a` after the specified removal.

