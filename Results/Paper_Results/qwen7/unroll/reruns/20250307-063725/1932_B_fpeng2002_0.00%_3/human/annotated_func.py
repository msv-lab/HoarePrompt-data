#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and a_1, a_2, ..., a_n are positive integers such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: The output state will consist of `num_tests` lines, each containing an integer representing the value of `start_year` calculated for each test case.
    #
    #Explanation: For each test case (indicated by the value of `num_tests`), the code reads an integer `n` and a list of `n` integers (`nums`). It then calculates the value of `start_year` based on the formula provided in the loop body. After calculating `start_year` for each test case, it prints the result. Therefore, after all iterations of the loop, there will be `num_tests` printed results, one for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `n` and a sequence of `n` positive integers `a_1, a_2, ..., a_n`. For each test case, it calculates and prints a value `start_year` based on the formula `((start_year + 1) // a[x] + 1) * a[x]`, starting with `start_year` initialized to 0. After processing all test cases, it outputs `num_tests` lines, each containing the calculated `start_year` for each respective test case.

