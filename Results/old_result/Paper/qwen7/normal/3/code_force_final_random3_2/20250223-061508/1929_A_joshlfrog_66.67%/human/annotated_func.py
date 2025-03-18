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
        
    #State: Output State: After the loop executes all iterations, `e` will be equal to `t-1`, `l` will be the total length of the list `nums` for each iteration, `i` will be `l-1`, `x` will be the maximum value found across all lists `nums` during the iterations, and `y` will be the minimum value found across all lists `nums` during the iterations.
    #
    #This means that after the loop has completed all its iterations, `e` will have reached `t-1`, indicating that the loop has executed `t` times. For each iteration, `l` is set to the length of the input list `nums`, `i` iterates from `0` to `l-1`, updating `x` to the highest value and `y` to the lowest value in each list `nums`. The final values of `x` and `y` will be the overall maximum and minimum values found across all the lists `nums` provided as inputs during the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. It finds the maximum and minimum values in each list and calculates the difference between these values. The function prints this difference for each test case. After processing all test cases, it outputs the differences for all cases.

