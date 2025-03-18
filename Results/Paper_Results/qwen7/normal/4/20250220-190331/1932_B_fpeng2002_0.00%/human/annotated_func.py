#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a list of n integers a_1, a_2, a_3, …, a_n where 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: `x` is equal to the length of the `nums` list, `start_year` is the result of applying the formula (((((...((start_year + 1) // nums[x-1]) + 1) * nums[x-1]) + 1) // nums[x-2] + 1) * nums[x-2]) + ... + 1) // nums[1] + 1) * nums[1] + 1) // nums[0] + 1) * nums[0] to the initial value of `start_year`, which is 0.
    #
    #In simpler terms, after the loop has executed all its iterations, the variable `x` will be equal to the length of the `nums` list, and `start_year` will be the final computed value after repeatedly applying the given formula to each element in the `nums` list from the last element to the first element, starting with `start_year` initialized to 0.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then computes a value `start_year` using a specific formula that involves dividing and multiplying the elements of the list in reverse order, starting with an initial value of 0. After processing all test cases, the function prints the computed `start_year` values for each test case.

