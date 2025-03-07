#State of the program right berfore the function call: The function `func` is expected to be part of a larger program that processes multiple test cases. Each test case includes an integer `n` (2 ≤ n ≤ 50) representing the number of cells in the ribbon, and a list of integers `a` of length `n` where each element is either 0 (free cell) or 1 (cell with a chip). At least one cell in each test case contains a chip. The function should be called with the appropriate parameters for each test case.
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
        
    #State: `t` is 0, `_` is `t - 1`, `n` is an input integer, `a` is a list of integers with all leading zeros removed and all trailing zeros removed, `i` is `len(a) - 1`, and `res` is the number of zeros in the list `a` for the last test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of length `n` containing integers (0 or 1). It then removes all leading and trailing zeros from the list `a` and counts the number of zeros remaining in the list. The function prints the modified list `a` and the count of zeros for each test case. After processing all test cases, the function does not return any value. The final state of the program is that `t` is 0, `_` is `t - 1`, `n` is the last input integer, `a` is the last modified list with leading and trailing zeros removed, `i` is `len(a) - 1`, and `res` is the number of zeros in the last modified list `a`.

