#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases, and a list of lists, where each inner list contains integers n and a list of n integers a_1, a_2, ..., a_n. For each test case, t is in the range 1 ≤ t ≤ 1000, n is in the range 1 ≤ n ≤ 100, and each a_i is in the range 1 ≤ a_i ≤ 10^6.
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
        
    #State: `num_tests` is 0, `n` is the last input integer, `nums` is the last list of integers provided by the user that must have at least one element, `start_year` is the smallest multiple of the last `nums[len(nums) - 1]` that is greater than or equal to the value of `start_year` after the previous iteration plus 1, `x` is `len(nums) - 1`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers from the user. It then calculates the smallest year that is a multiple of each integer in the list and is greater than or equal to the previous year plus one. The function prints the calculated year for each test case. After processing all test cases, the function concludes with `num_tests` being 0. The function does not return any value.

