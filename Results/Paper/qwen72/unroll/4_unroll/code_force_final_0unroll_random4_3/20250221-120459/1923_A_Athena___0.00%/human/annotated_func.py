#State of the program right berfore the function call: The function `func` is expected to be called with specific parameters for the problem, but the function definition provided does not include these parameters. For the problem described, the function should accept an integer `t` representing the number of test cases, and for each test case, it should accept an integer `n` representing the number of cells, and a list `a` of length `n` containing integers 0 or 1, where 0 represents a free cell and 1 represents a cell with a chip. Additionally, `t` is an integer such that 1 <= t <= 1000, `n` is an integer such that 2 <= n <= 50, and `a` contains at least one chip (1).
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `n` is the last input integer such that 2 <= n <= 50, and `a` is the last non-empty list of integers after removing leading and trailing zeros.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list `a` of length `n` containing integers 0 or 1. The function then removes leading and trailing zeros from the list `a` and prints the modified list. It calculates and prints the number of zeros remaining in the list `a` after the removal of leading and trailing zeros. The function does not return any value. After the function concludes, `t` is an integer such that 1 <= t <= 1000, `n` is the last input integer such that 2 <= n <= 50, and `a` is the last non-empty list of integers after removing leading and trailing zeros.

