#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. Each test case consists of an integer n such that 2 ≤ n ≤ 100, followed by a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for all i.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: Output State: After executing the loop for all test cases, the output state will consist of a list of differences between the maximum and minimum values for each test case. For each test case, the program sorts the list of integers and then prints the difference between the largest and smallest number in the sorted list.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer n and a list of n integers. For each test case, it sorts the list of integers and calculates the difference between the largest and smallest numbers in the sorted list. It then prints this difference for each test case. After processing all test cases, the function concludes with no explicit return value, but outputs the differences for each test case.

