#State of the program right berfore the function call: The function should be called with a list of test cases, where each test case is a list containing an integer n (1 ≤ n ≤ 100) followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6).
def func():
    num_tests = int(input())
    while num_tests > 0:
        num_tests -= 1
        
        n = int(input())
        
        nums = [int(x) for x in input().split(' ')]
        
        start_year = 0
        
        for x in range(0, len(nums)):
            start_year = ((start_year + 1) // nums[x] + 1) * nums[x]
        
        print(start_year)
        
    #State: `num_tests` is 0, `n` is an input integer, `nums` is a list of `n` integers provided as input, `start_year` is the smallest multiple of the last element in `nums` that is greater than or equal to the cumulative result of the smallest multiples of all previous elements in `nums`, `x` is `len(nums) - 1`.
#Overall this is what the function does:The function `func` reads a series of test cases from the standard input. Each test case consists of an integer `n` followed by a list of `n` integers. For each test case, the function calculates the smallest year that is a multiple of each integer in the list, where the year is greater than or equal to the cumulative result of the smallest multiples of all previous integers in the list. The function prints the calculated year for each test case. After processing all test cases, `num_tests` is 0, `n` is the last input integer, `nums` is the last list of `n` integers, and `start_year` is the calculated year for the last test case.

