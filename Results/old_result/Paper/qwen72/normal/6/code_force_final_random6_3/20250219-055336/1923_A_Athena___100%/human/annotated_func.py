#State of the program right berfore the function call: The function `func` is expected to be called within a loop or context that handles multiple test cases, where each test case consists of an integer `n` (2 ≤ n ≤ 50) representing the number of cells in the ribbon, and a list of integers `a` of length `n` where each element is either 0 (free cell) or 1 (cell with a chip), and at least one cell contains a chip.
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
        
    #State: `a` is a list of integers with all leading zeros removed and all trailing zeros removed, `i` is the index of the last element of `a`, `t` is 0, `n` is an input integer, and `res` is the number of zeros in the list `a` for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list of integers `a` of length `n`, where each element is either 0 (free cell) or 1 (cell with a chip). It then removes leading and trailing zeros from the list `a` and counts the number of zeros remaining in the list. The function prints the count of zeros for each test case. After processing all test cases, the function concludes, and the state of the program is such that all test cases have been processed, and the counts of zeros for each test case have been printed.

