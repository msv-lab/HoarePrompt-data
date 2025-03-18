#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and the following list contains n integers a_1, a_2, a_3, \dots, a_n such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: The output state will be a list of integers, each representing the value of `start_year` after processing each input test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n` and a list of `n` integers. It then calculates a starting year based on the given integers and prints the result. The function reads input from the standard input, processes up to 1000 test cases, and outputs a list of calculated starting years, one for each test case.

