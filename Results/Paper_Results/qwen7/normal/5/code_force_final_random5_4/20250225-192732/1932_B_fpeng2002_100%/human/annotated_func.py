#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a list of n integers a_1, a_2, a_3, …, a_n where 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: `num_tests` is 0, `n` is an input integer, `nums` is a list of integers with at least one element, `x` is equal to the length of `nums`, and `start_year` is the result of applying the formula `(start_year // nums[x-1] + 1) * nums[x-1]` for each `x` from 0 to the length of `nums` minus one, iteratively.
    #
    #In simpler terms, after the loop has executed all its iterations, `num_tests` will be 0 because it is decremented by 1 in each iteration until it reaches 0. The variable `n` remains unchanged as it is not affected by the loop. `nums` is a list of integers that must have at least one element, and `x` will be equal to the length of `nums`. The variable `start_year` will be the final value obtained by successively applying the operation `(start_year // nums[x-1] + 1) * nums[x-1]` to each element in the `nums` list, starting from an initial `start_year` of 0 and iterating over all elements in the list.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers `a_1, a_2, ..., a_n`. It then calculates a value `start_year` by iteratively applying the formula `(start_year // a_i + 1) * a_i` for each element `a_i` in the list, starting with `start_year` initialized to 0. After processing all test cases, it prints the final `start_year` value for each test case.

