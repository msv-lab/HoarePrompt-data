#State of the program right berfore the function call: The function `func` is expected to be called within a context where it processes multiple test cases. Each test case consists of an integer `n` (2 ≤ n ≤ 50) representing the number of cells in the ribbon, and a list of integers `a` of length `n` where each element is either 0 or 1, representing whether a cell is free or contains a chip, respectively. At least one cell in each test case contains a chip.
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
        
    #State: The loop has processed all `t` test cases, and for each test case, it has printed the number of free cells (`0`s) between the first and last chip (`1`s) in the ribbon. The variables `n`, `a`, and `res` are reset and redefined for each test case, so their final values are not meaningful outside the context of the last test case processed.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` (2 ≤ n ≤ 50) and a list `a` of length `n` containing 0s and 1s. For each test case, it calculates and prints the number of free cells (0s) between the first and last chip (1s) in the ribbon. The function does not return any value. After processing all test cases, the variables `n`, `a`, and `res` are in the state of the last test case processed, but their values are not meaningful outside this context.

