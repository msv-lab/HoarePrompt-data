#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: After the loop executes all its iterations, `t` is a positive integer such that \(1 \leq t \leq 500\), `e` will be equal to `t-1` (since the loop runs from `e` in range `t`), `l` is the length of the list `nums`, `x` is the maximum value in the list `nums`, and `y` is the minimum value in the list `nums`.
    #
    #Explanation:
    #- The variable `t` remains within the range \(1 \leq t \leq 500\) as it was initially set.
    #- The variable `e` will be equal to `t-1` because the loop runs from `e` in the range `t`.
    #- The variable `l` is set to the length of the list `nums` when the loop starts.
    #- The variable `x` is updated during each iteration to hold the maximum value encountered in the list `nums`.
    #- The variable `y` is updated during each iteration to hold the minimum value encountered in the list `nums`.
    #
    #After all iterations of the loop, `x` will contain the highest value in the list `nums`, and `y` will contain the lowest value in the list `nums`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t` representing the number of subsequent test cases, then for each test case, it reads an integer `n` and a list of `n` integers. It finds the maximum and minimum values in the list of integers and prints the difference between these two values. After processing all test cases, the function does not return any value but prints the result for each test case.

