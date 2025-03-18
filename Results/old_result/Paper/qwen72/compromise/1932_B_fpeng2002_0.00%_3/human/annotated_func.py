#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases (1 ≤ t ≤ 1000), and a list of lists, where each inner list contains n integers a_1, a_2, a_3, ..., a_n (1 ≤ n ≤ 100 and 1 ≤ a_i ≤ 10^6) representing the periodicities of the signs for each test case.
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
        
    #State: `num_tests` is 0, `start_year` is the smallest multiple of the last element in `nums` that is greater than the previous `start_year` for each `x` in `range(0, len(nums))` for all test cases, and `n` and `nums` have been processed for all test cases.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `nums` representing periodicities. It calculates and prints the smallest year that is a multiple of each periodicity in `nums` and is greater than the previous calculated year for each periodicity in the list. After processing all test cases, the function ends with `num_tests` set to 0, and all input values processed. The function does not return any value.

