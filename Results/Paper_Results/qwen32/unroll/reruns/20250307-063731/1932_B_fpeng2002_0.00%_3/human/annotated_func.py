#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 1000) indicating the number of test cases. Each test case consists of two lines: the first line contains an integer n (1 ≤ n ≤ 100) representing the number of signs, and the second line contains n integers a_1, a_2, a_3, ..., a_n (1 ≤ a_i ≤ 10^6) representing the periodicities of the signs.
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
        
    #State: num_tests is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of signs and their respective periodicities. For each test case, it calculates and prints the earliest year in which all signs will be synchronized based on their periodicities.

