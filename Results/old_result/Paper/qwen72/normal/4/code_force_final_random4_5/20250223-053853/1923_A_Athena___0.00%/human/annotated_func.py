#State of the program right berfore the function call: The function `func` is expected to be called within a loop or similar construct that handles multiple test cases. Each test case includes an integer `n` (2 ≤ n ≤ 50) representing the number of cells in the ribbon, and a list `a` of `n` integers (0 ≤ a_i ≤ 1) where `a_i = 0` indicates a free cell and `a_i = 1` indicates a cell containing a chip. At least one cell in each test case contains a chip.
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
        
    #State: After all iterations of the loop, the variable `t` will be 0, and the variables `n`, `a`, and `res` will have their final values from the last test case. The list `a` will be modified to remove leading and trailing zeros, and `res` will contain the count of zeros in the modified list `a`.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case involves an integer `n` and a list `a` of `n` integers. The function reads the number of test cases `t` from the input, and for each test case, it reads `n` and `a`. It then modifies the list `a` by removing leading and trailing zeros. After the modifications, it counts the number of zeros remaining in the list `a` and prints this count. The function does not return any value; it only prints the results. After all test cases are processed, the variable `t` will be 0, and the variables `n`, `a`, and `res` will hold their final values from the last test case.

