#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a_1, a_2, a_3, \dots, a_n are integers such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: `x` is 0, `start_year` is (((((...(((start_year + 1) // nums[0] + 1) * nums[0]) + 1) // nums[1] + 1) * nums[1]) + 1) // nums[2] + 1) * nums[2] ... // nums[len(nums)-2] + 1) * nums[len(nums)-2]) // nums[len(nums)-1] + 1) * nums[len(nums)-1], `num_tests` is 0, `nums` is a list of integers obtained from input, `n` is an input integer.
    #
    #In natural language: After the loop executes all its iterations, the variable `x` will be 0 because the loop decrements `x` until it reaches 0. The variable `start_year` will be updated through a series of operations involving each element in the `nums` list, starting from the last element and moving towards the first. Specifically, `start_year` will be calculated as (((((...(((start_year + 1) // nums[0] + 1) * nums[0]) + 1) // nums[1] + 1) * nums[1]) + 1) // nums[2] + 1) * nums[2] ... // nums[len(nums)-2] + 1) * nums[len(nums)-2]) // nums[len(nums)-1] + 1) * nums[len(nums)-1]. The variable `num_tests` will be 0 because the loop decrements `num_tests` by 1 in each iteration until it becomes 0. The lists `nums` and the integer `n` remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer n and a sequence of n integers. It then calculates a value `start_year` based on these integers using a specific formula and prints the result. After processing all test cases, it outputs the calculated `start_year` values for each case.

