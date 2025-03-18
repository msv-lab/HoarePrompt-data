#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases (1 ≤ t ≤ 1000), and a list of lists, where each inner list contains n integers (1 ≤ n ≤ 100) representing the periodicities of the signs (1 ≤ a_i ≤ 10^6).
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
        
    #State: `num_tests` is 0, and the loop has printed the value of `start_year` for each iteration, which represents the first year in which all signs in the list `nums` align according to their periodicities.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers from the input, representing the periodicities of certain signs. The function calculates the first year in which all signs align according to their periodicities and prints this year for each test case. After processing all test cases, the function ensures that `num_tests` is 0. The function does not return any value.

