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
        
    #State: `t` is an input integer where 1 <= t <= 500, `e` is `t-1`, `l` is the last input integer, `nums` is the last list of integers input by the user, `i` is `l-1`, `x` is the maximum value in the last `nums`, and `y` is the minimum value in the last `nums`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, where `1 <= t <= 500`. It then processes `t` test cases. For each test case, it reads an integer `l` (where `2 <= l <= 100`) and a list of `l` integers. The function computes and prints the difference between the maximum and minimum values in the list for each test case. After processing all test cases, the final state of the program is that `t` test cases have been processed, and the differences between the maximum and minimum values of each list have been printed.

