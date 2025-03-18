#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a list of n integers a_1, a_2, a_3, …, a_n such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: The output state will be a list of integers where each integer represents the value of `start_year` calculated for each test case.
    #
    #Explanation: For each test case specified by `num_tests`, the code reads an integer `n` and a list of `n` integers from the input. It then iterates through the list, calculating `start_year` based on the formula provided. After processing all test cases, it prints the final value of `start_year` for each test case. Therefore, the output will consist of one line per test case, with each line containing the computed `start_year` value for that specific test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it calculates a value `start_year` using a specific formula and prints this value. The function reads inputs from standard input and outputs the calculated values to standard output, resulting in a list of integers where each integer corresponds to the `start_year` value for each test case.

