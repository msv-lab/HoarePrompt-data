#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, n is an integer such that 2 <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
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
        
    #State: `t` is an input integer such that 1 <= t <= 500, `e` is `t-1`, `l` is the last input integer, `nums` is the last list of integers input by the user, `i` is `l-1`, `x` is the maximum value in the last list `nums`, and `y` is the minimum value in the last list `nums`.
#Overall this is what the function does:The function reads an integer `t` from the user, where `1 <= t <= 500`. For each of the `t` test cases, it reads another integer `l` (which is not necessarily the same as `n`), where `2 <= l <= 100`, and a list of `l` integers, each between `1` and `10^9`. It then calculates the difference between the maximum and minimum values in the list and prints this difference. After processing all `t` test cases, the function completes, and the final state of the program is that `t` test cases have been processed, and the differences between the maximum and minimum values of each list have been printed.

