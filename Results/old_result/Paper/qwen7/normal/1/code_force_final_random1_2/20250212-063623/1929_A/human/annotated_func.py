#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: Output State: After the loop executes all the iterations, `ntest` is an input integer, `itest` is equal to `ntest`, `a` is a sorted list of integers obtained from splitting the input string and converting each element to an integer for each iteration, and `n` is an input integer for each iteration.
    #
    #In simpler terms, after the loop has completed all its iterations, `ntest` will be the last value it was set to, which is also the number of times the loop ran. The variable `a` will hold the sorted list of integers from the last input, and `n` will be the last input integer processed.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer n and a list of n integers a_1, a_2, ..., a_n. For each test case, it sorts the list of integers and calculates the difference between the largest and smallest integers in the sorted list. It then prints this difference for each test case. After processing all test cases, the function does not return any value but outputs the differences for each test case.

