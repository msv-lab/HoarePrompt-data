#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 100) representing the number of signs. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the periodicities of the signs. The number of test cases t is between 1 and 1000.
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
        
    #State: `num_tests` is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of signs and their respective periodicities, and prints the first common year when all signs will be active again starting from year 0.

