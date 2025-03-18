#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a list of n integers a_1, a_2, a_3, \dots, a_n such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: `start_year` will be equal to the final value obtained by successively applying the formula `(start_year // nums[x] + 1) * nums[x]` for each element in the `nums` list, with `x` taking the value of the last index of `nums` after all iterations.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates a value `start_year` by successively applying the formula `(start_year // nums[x] + 1) * nums[x]` for each element in the list `nums`. After processing all test cases, it prints the final value of `start_year` for the last test case.

