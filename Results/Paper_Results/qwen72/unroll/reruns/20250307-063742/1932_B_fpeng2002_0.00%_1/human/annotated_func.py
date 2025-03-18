#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 1000), n is a positive integer (1 ≤ n ≤ 100), and a is a list of n positive integers (1 ≤ a_i ≤ 10^6).
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
        
    #State: num_tests is 0, n is the last input integer, nums is the last list of n integers, start_year is the calculated start year for the last test case, t is unchanged, a is unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads multiple test cases from the standard input, where each test case consists of an integer `n` followed by a list of `n` positive integers. For each test case, it calculates a start year based on the provided list of integers and prints the result. After processing all test cases, the function terminates with `num_tests` set to 0, and the last processed `n` and `nums` retained. The variables `t` and `a` mentioned in the annotations are not used or modified by the function.

