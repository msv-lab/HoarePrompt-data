#State of the program right berfore the function call: The function `func` is expected to take input parameters, but the function definition provided does not include any. The correct function definition should include parameters for the number of test cases `t`, the length of the array `n`, and the array `a` itself. The correct function definition should be: `def func(t, n, a):` where `t` is an integer such that 1 <= t <= 500, `n` is an integer such that 2 <= n <= 100, and `a` is a list of integers such that 1 <= a_i <= 10^9 for all 1 <= i <= n.
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
        
    #State: `t` is greater than 0, `e` is `t-1`, `l` is the last input integer, `i` is `l-1`, `nums` is the last list of integers provided by the user, `x` is the maximum value in the last `nums`, and `y` is the minimum value in the last `nums`.
#Overall this is what the function does:The function `func` reads input from the user to process multiple test cases. For each test case, it reads an integer `l` representing the length of an array, followed by `l` integers that form the array. It then calculates the difference between the maximum and minimum values in the array and prints this difference. After processing all test cases, the function completes without returning any value. The final state of the program includes the variables `t` (the number of test cases), `e` (the index of the last processed test case, which is `t-1`), `l` (the length of the last array), `i` (the index of the last element processed in the last array, which is `l-1`), `nums` (the last array of integers provided by the user), `x` (the maximum value in the last `nums`), and `y` (the minimum value in the last `nums`).

