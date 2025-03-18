#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: t is an integer between 1 and 500 (inclusive), and it is now set to the value it was initially. The variable `l` is an integer, which changes with each iteration but is reset to the value of `l` for each new input. The variable `nums` is a list of integers, which changes with each iteration but is reset to the new list of integers for each new input. The variables `x` and `y` are integers that are updated during the inner loop for each input list but are reset to their initial values (0 for `x` and 100000000 for `y`) for each new input. After all iterations, the final value of `x - y` is printed, which is the difference between the maximum and minimum values in the last input list.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( t \) indicating the number of sub-cases. For each sub-case, it reads another integer \( n \) and a list of \( n \) integers. It then calculates and prints the difference between the maximum and minimum values in the list for each sub-case. After processing all sub-cases, the function concludes with no explicit return value but outputs the differences for each sub-case.

