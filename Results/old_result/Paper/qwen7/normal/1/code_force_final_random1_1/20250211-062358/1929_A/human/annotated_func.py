#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: Output State: After the loop executes all iterations, `ntest` must be a positive integer, `itest` will be equal to `ntest - 1`, indicating that the loop has completed all its iterations. For each iteration, `n` is an input integer, and `a` is a list of sorted integers obtained from splitting the input string and converting each element to an integer. The final output of the program will be the difference between the maximum and minimum values of each list `a` for all iterations.
    #
    #This means that after all iterations, the program will have processed all test cases provided by the value of `ntest`, and for each test case, it will have printed the difference between the largest and smallest numbers in the list `a`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer \( n \) and a list of \( n \) integers. It sorts the list and calculates the difference between the maximum and minimum values in the sorted list. The function prints this difference for each test case. After processing all test cases, it does not return any value.

