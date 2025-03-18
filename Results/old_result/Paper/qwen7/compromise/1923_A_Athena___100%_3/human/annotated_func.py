#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and the second line contains a list of n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. Additionally, in each test case, at least one cell contains a chip.
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
        
    #State: Output State: After all iterations of the loop have finished, the variable `t` will be reduced by 6 times the sum of all `n` values entered initially. The list `a` will be empty after all leading and trailing zeros have been removed from each `a` list during each iteration. The variable `res` will be the total count of all zeros present in all the lists `a` across all iterations.
    #
    #This means that `t` will reflect the remaining number of iterations after accounting for all the iterations performed based on the input values of `n`. The `res` variable will hold the cumulative count of zeros from all the processed lists `a`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` (number of test cases), an integer `n`, and a list of `n` binary values (0s and 1s). It then removes any leading and trailing zeros from the list and counts the remaining zeros. Finally, it prints the total count of zeros across all test cases.

