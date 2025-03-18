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
        
    #State: `num_tests` is 0, `n` is the last input integer read, `nums` is the last list of integers read, and `start_year` is the last computed start year based on the last list of integers read. The values of `t` and `a` remain unchanged.
#Overall this is what the function does:The function `func` reads multiple sets of inputs from the user. For each set, it first reads an integer `n`, then reads a list of `n` integers. It computes the smallest year that is a multiple of all the integers in the list and prints this year. After processing all sets of inputs, the function ensures that `num_tests` is 0, and the last processed values of `n` and `nums` remain as they were for the final set. The function does not accept any parameters and does not return any values. The initial state of `t` and `a` remains unchanged.

