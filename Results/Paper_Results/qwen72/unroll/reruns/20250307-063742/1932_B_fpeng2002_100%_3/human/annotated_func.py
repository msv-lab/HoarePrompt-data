#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 1 ≤ n ≤ 100, and a_i is an integer such that 1 ≤ a_i ≤ 10^6 for each i in the range 1 to n.
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
        
    #State: `num_tests` is 0, `n` is an integer such that 1 ≤ n ≤ 100, `nums` is a list of integers such that 1 ≤ a_i ≤ 10^6 for each i in the range 1 to n, `start_year` is the smallest multiple of the largest number in `nums` that is greater than or equal to the largest multiple of the smallest number in `nums` that is less than or equal to the initial `start_year`.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` integers `nums`. It then calculates the smallest year that is a multiple of all the integers in `nums` and prints this year. After processing all test cases, the function terminates with `num_tests` set to 0.

