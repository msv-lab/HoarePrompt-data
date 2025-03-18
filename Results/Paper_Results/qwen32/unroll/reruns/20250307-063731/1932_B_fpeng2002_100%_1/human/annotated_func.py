#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, for each test case, n is an integer such that 1 <= n <= 100, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^6.
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
        
    #State: num_tests is 0, t remains unchanged, n and nums are not retained, start_year is not retained.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it calculates and prints a specific year based on a list of integers provided. The input consists of the number of test cases, followed by the number of integers and the integers themselves for each test case. The output is the calculated year for each test case.

