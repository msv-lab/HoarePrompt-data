#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, and a is a list of n integers where 1 ≤ a_i ≤ 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: `t` is an integer where 1 ≤ t ≤ 500, `n` is an input integer where 2 ≤ n ≤ 100, `a` is a sorted list of integers, `ntest` must be equal to the initial value of `ntest`, `itest` is `ntest - 1`.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case consists of an integer `n` followed by a list of `n` integers. For each test case, the function sorts the list of integers and then prints the difference between the largest and smallest numbers in the sorted list. After processing all test cases, the function ends without returning any value. The state of the program after the function concludes includes the processed test cases, with the final value of `ntest` (the number of test cases) remaining unchanged, and `itest` being equal to `ntest - 1`.

