#State of the program right berfore the function call: The function is expected to handle multiple test cases. For each test case, the input includes an integer n (2 ≤ n ≤ 50) representing the number of cells in the ribbon, and a list of n integers (0 or 1) representing the state of each cell, where 0 means the cell is free and 1 means the cell contains a chip. The input is provided in a structured format where the first line contains the number of test cases t (1 ≤ t ≤ 1000), followed by t test cases, each consisting of two lines as described. In each test case, at least one cell contains a chip.
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
        
        print(a)
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: `t` is 0, `_` is `t-1` (which is the last iteration index), `n` is an input integer, `a` is a list of integers from the last input with all leading zeros and trailing zeros removed, `i` is the length of the last `a` minus 1, and `res` is the number of zeros in the last `a`.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case involves an integer `n` (2 ≤ n ≤ 50) representing the number of cells in a ribbon, and a list of `n` integers (0 or 1) representing the state of each cell (0 for free, 1 for a chip). For each test case, the function removes all leading and trailing zeros from the list, prints the modified list, counts the number of zeros remaining in the list, and prints this count. After processing all test cases, the function concludes, and the final state of the program is that all test cases have been processed and the results (modified lists and zero counts) have been printed. The function does not return any values.

