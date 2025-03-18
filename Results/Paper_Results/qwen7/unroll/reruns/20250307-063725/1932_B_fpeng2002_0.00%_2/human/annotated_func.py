#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and a_1, a_2, a_3, \dots, a_n are positive integers such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: The output state will be a list of integers, where each integer represents the value of `start_year` calculated for each test case.
    #
    #Explanation: For each test case specified by the input integer `num_tests`, the code calculates a value for `start_year` based on the list of integers provided as input. The calculation involves iterating over the list of integers and applying a specific formula to determine `start_year`. After processing all test cases, the output consists of the final `start_year` value for each test case printed in sequence.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `n` and a list of `n` positive integers. For each test case, it calculates a value for `start_year` using a specific formula involving the elements of the list. The function prints the calculated `start_year` for each test case.

