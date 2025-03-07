#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: Output State: The maximum difference between the largest and smallest numbers among the inputs provided for each iteration, up to a total of ntest iterations, where 1 ≤ ntest ≤ 500.
#Overall this is what the function does:The function processes multiple test cases, each containing a positive integer t and a list of n integers. For each test case, it calculates and outputs the difference between the largest and smallest numbers in the list. The function iterates up to a maximum of 500 test cases.

