#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, and a_i are integers such that 1 <= a_i <= 10^6 for each i from 1 to n.
def func():
    num_tests = int(input())
    while num_tests > 0:
        num_tests -= 1
        
        n = int(input())
        
        nums = [int(x) for x in input().split(' ')]
        
        start_year = 0
        
        for x in range(0, len(nums)):
            start_year = (start_year // nums[x] + 1) * nums[x]
        
        print(start_year)
        
    #State: `t` is an integer such that 1 <= t <= 1000, `n` is an input integer such that 1 <= n <= 100, `a_i` are integers such that 1 <= a_i <= 10^6 for each i from 1 to n, `num_tests` is 0, `nums` is a list of `n` integers provided by the user input for each iteration, `x` is `n-1` for the last iteration, `start_year` is the smallest multiple of the product of all elements in `nums` for the last iteration that is greater than or equal to the initial `start_year`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `nums`. It calculates the smallest multiple of each element in `nums` that is greater than or equal to the initial `start_year` (which is 0) and prints this value. After processing all test cases, `num_tests` is 0, and the function has no return value. The function does not modify the input variables `t`, `n`, or `nums`.

