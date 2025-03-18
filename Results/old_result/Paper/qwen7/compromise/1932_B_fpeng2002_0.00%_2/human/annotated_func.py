#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and the list a contains n integers such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: `x` is equal to the length of the `nums` list, and `start_year` is the result of applying the operation `((start_year + 1) // nums[x] + 1) * nums[x]` for each index `x` from 0 to the length of the `nums` list minus one, with `x` being equal to the length of the `nums` list minus one after all iterations.
    #
    #In simpler terms, after the loop has executed all its iterations, `x` will be equal to the length of the `nums` list. The variable `start_year` will hold the final value obtained by successively applying the formula `((start_year + 1) // nums[x] + 1) * nums[x]` for each index `x` from 0 to the length of the `nums` list minus one. This means that `start_year` will undergo a series of updates, each time incorporating the next element in the `nums` list, until all elements have been processed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the number of integers in a list `a`, and the list `a` itself containing `n` integers. For each test case, it calculates a final value for `start_year` by iteratively applying a specific formula to each element in the list `a`. The final value of `start_year` is then printed for each test case.

