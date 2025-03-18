#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6.
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
        
    #State: `num_tests` is 0, `n` remains an integer such that 1 ≤ n ≤ 100, `a` remains a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6, and `start_year` is the smallest integer that is a multiple of all integers in the list `nums` for the last iteration of the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `nums`. It calculates the smallest integer `start_year` that is a multiple of all integers in `nums` for the last iteration of the loop and prints this value. After processing all test cases, `num_tests` is 0, `n` remains an integer such that 1 ≤ n ≤ 100, and `nums` remains a list of `n` integers where each integer satisfies 1 ≤ a_i ≤ 10^6. The function does not return any value.

