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
        
    #State: Output State: `t` is an integer between 1 and 500 inclusive, `e` is equal to `t`, `l` is the length of the `nums` list, `nums` is a list of integers obtained from splitting the input string on spaces, `x` is the maximum value found in the `nums` list during the loop's execution, and `y` is the minimum value found in the `nums` list during the loop's execution.
    #
    #Explanation: After the loop has executed all its iterations, `e` will be equal to `t` because the loop runs `t` times. The variable `l` will remain unchanged as it is not affected by the loop. The variable `x` will hold the maximum value found in the `nums` list across all the lists processed by the loop. Similarly, the variable `y` will hold the minimum value found in the `nums` list across all the lists processed by the loop. The other variables (`t` and `nums`) remain unchanged as they are not affected by the loop body.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) (1 ≤ \( t \) ≤ 500) and a list of \( n \) integers (2 ≤ \( n \) ≤ 100). For each test case, it finds the maximum and minimum values in the list of integers, calculates the difference between these two values, and prints the result. After processing all test cases, it outputs the differences for each case.

