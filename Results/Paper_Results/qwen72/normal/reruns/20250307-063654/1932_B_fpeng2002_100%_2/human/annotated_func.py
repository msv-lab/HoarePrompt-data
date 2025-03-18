#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, n is a positive integer such that 1 <= n <= 100, and a is a list of n positive integers such that 1 <= a_i <= 10^6.
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
        
    #State: `t` is a positive integer such that 1 <= t <= 1000, `n` is the last input integer, `a` is a list of n positive integers such that 1 <= a_i <= 10^6, `num_tests` is 0, `nums` is the last list of integers input by the user that must have at least `len(nums)` elements, `start_year` is the smallest multiple of the last element in `nums` that is greater than or equal to the original `start_year`, and this `start_year` is the result of applying the same logic for each element in `nums` sequentially.
#Overall this is what the function does:The function `func` reads a series of test cases from user input. For each test case, it reads an integer `n` and a list of `n` positive integers. It then calculates the smallest year that is a multiple of each integer in the list, starting from 0, and prints this year. After processing all test cases, the function concludes with `num_tests` set to 0. The function does not return any value.

