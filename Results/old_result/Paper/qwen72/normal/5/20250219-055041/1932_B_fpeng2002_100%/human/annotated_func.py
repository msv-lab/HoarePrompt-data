#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `n` is an input integer, `a` is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, `num_tests` is 0, `start_year` is the smallest multiple of the last element in `nums` that is greater than or equal to the smallest multiple of the second-to-last element in `nums` that is greater than or equal to the smallest multiple of the third-to-last element in `nums` and so on, up to the smallest multiple of `nums[0]` that is greater than or equal to 0, `nums` is a non-empty list of integers input by the user, `x` is `len(nums) - 1`.
#Overall this is what the function does:The function `func` reads an integer `num_tests` indicating the number of test cases. For each test case, it reads an integer `n` and a list `nums` of `n` integers. It calculates the smallest year that is a multiple of each integer in `nums` in sequence, starting from 0, and prints this year. After processing all test cases, `num_tests` is 0, and the function does not return any value.

