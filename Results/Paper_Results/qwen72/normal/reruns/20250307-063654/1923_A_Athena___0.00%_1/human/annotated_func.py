#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an integer `n` (2 ≤ n ≤ 50) representing the number of cells in the ribbon, and a list of integers `a` of length `n` where each element `a_i` is either 0 or 1, representing whether the i-th cell is free (0) or contains a chip (1). At least one cell in each test case contains a chip. The function should be called multiple times, each time with a different test case, and the number of test cases `t` is an integer (1 ≤ t ≤ 1000).
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
        
    #State: `t` is 0, `n` is an input integer, `a` is a list of integers with all leading zeros removed and all trailing zeros removed, `res` is the number of zeros in the list `a`, `i` is the last index of the list `a` (i.e., `len(a) - 1`).
#Overall this is what the function does:The function `func` processes multiple test cases. Each test case involves an integer `n` (2 ≤ n ≤ 50) and a list `a` of length `n` containing integers 0 or 1. The function removes all leading and trailing zeros from `a`, then counts the number of zeros remaining in the list. It prints the modified list `a` and the count of zeros for each test case. After processing all test cases, the function does not return any value.

