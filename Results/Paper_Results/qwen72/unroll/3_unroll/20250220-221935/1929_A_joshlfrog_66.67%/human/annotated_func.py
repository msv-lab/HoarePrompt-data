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
        
    #State: For each iteration of the loop, the maximum value (`x`) and the minimum value (`y`) from the list `nums` are found, and the difference `x - y` is printed. After all iterations, the values of `t`, `n`, and `a` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 500`. For each of the `t` test cases, it reads an integer `l` (which is not used in the function) and a list of integers `nums` from the input. It then calculates the difference between the maximum and minimum values in `nums` and prints this difference. The function does not return any value. After all iterations, the values of `t`, `n`, and `a` (if they exist outside the function) remain unchanged.

