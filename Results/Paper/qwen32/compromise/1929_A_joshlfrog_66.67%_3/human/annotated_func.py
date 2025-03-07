#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
def func():
    t = int(input())
    for e in range(t):
        l = int(input())
        
        nums = [int(x) for x in input().split()]
        
        x = 0
        
        y = 100000000
        
        for i in range(l):
            if nums[i] > x:
                x = nums[i]
            if nums[i] < y:
                y = nums[i]
        
        print(x - y)
        
    #State: `t` is an integer such that 1 <= t <= 500, `n` is an integer such that 2 <= n <= 100, `a` is a list of `n` integers where each integer `a_i` satisfies 1 <= `a_i` <= 10^9, and the loop has completed `t` iterations. For each iteration `e` (where 0 <= e < t), an integer `l` was read, followed by a list `nums` of `l` integers. The loop printed the difference between the maximum (`x`) and minimum (`y`) values in `nums` for each iteration.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it reads an integer `l` and a list of `l` integers. It then calculates and prints the difference between the maximum and minimum values in the list for each test case.

