#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
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
        
    #State: The variable `t` remains unchanged, `n` remains unchanged, and `a` remains unchanged. For each of the `t` iterations, the difference between the maximum and minimum values of the input list `nums` is printed.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of a list of integers. For each test case, it calculates and prints the difference between the maximum and minimum values in the list. The input integers and their counts remain unchanged throughout the function's execution.

