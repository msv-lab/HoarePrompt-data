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
        
    #State: `t` is an input integer such that 1 <= `t` <= 500; `e` is equal to `t`, indicating that the loop has executed `t` times; for each of the `t` iterations, the loop processed a list `nums` of length `l` with integers derived from the input, and for each list, it calculated `x` as the maximum value and `y` as the minimum value, printing `x - y`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then calculates and prints the difference between the maximum and minimum values in the list for each test case.

