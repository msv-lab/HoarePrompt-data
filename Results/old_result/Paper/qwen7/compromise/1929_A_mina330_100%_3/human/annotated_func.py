#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: Output State: The maximum difference between the largest and smallest numbers across all test cases. Each test case consists of an integer `n` followed by `n` space-separated integers, and the process is repeated `ntest` times.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` followed by `n` space-separated integers. For each test case, it sorts the list of integers and calculates the difference between the largest and smallest numbers. It then prints this difference for each test case. After processing all test cases, it outputs the maximum difference found across all test cases.

