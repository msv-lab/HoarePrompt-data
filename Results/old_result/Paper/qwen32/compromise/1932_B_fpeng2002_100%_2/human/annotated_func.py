#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 100, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^6.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000; `num_tests` is 0; `n` is the input integer from the last iteration; `nums` is a list of integers obtained by converting the space-separated input values to integers from the last iteration; `start_year` is the least common multiple (LCM) of all the integers in the `nums` list from the last iteration.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates and prints the least common multiple (LCM) of the integers in the list.

