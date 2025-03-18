#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 2 ≤ n ≤ 50; the second line of each test case contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1, indicating whether the i-th cell is free (0) or contains a chip (1); in each test case, at least one cell contains a chip.
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
        
    #State: Output State: After the loop executes all iterations, `res` will hold the total count of zeros in the final list `a` after all iterations. `_` will be equal to `t-1`, indicating that the loop has completed `t` iterations. `n` will still be the original input integer, and `a` will be an empty list if all elements were removed during the iterations or a list of non-zero integers otherwise. The variable `i` will be equal to the length of the final list `a`.
    #
    #This means that `res` will contain the cumulative count of zeros found in `a` across all iterations, and the list `a` will be processed to remove leading and trailing zeros, leaving only non-zero elements or an empty list if all elements were zeros.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( t \) (number of test cases), an integer \( n \) (number of cells), and a list of \( n \) integers indicating the state of each cell (0 for free, 1 for containing a chip). It then removes leading and trailing zeros from the list, counts the remaining zeros, and prints the count for each test case. After processing all test cases, it outputs the total count of zeros across all test cases.

