#State of the program right berfore the function call: t is an integer where 1 <= t <= 500, n is an integer where 2 <= n <= 100, and a is a list of n integers where 1 <= a_i <= 10^9.
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
        
    #State: The loop will print the difference between the maximum and minimum values of each list `nums` for `t` iterations. The values of `t` and `n` remain unchanged, and the list `a` is not affected by the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 500`. It then iterates `t` times, each time reading an integer `l` and a list of `l` integers from the input. For each list, it calculates and prints the difference between the maximum and minimum values. The function does not return any value. The values of `t` and `n` remain unchanged, and the list `a` is not affected by the function.

