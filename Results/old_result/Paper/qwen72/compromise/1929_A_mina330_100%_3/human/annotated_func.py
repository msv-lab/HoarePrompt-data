#State of the program right berfore the function call: t is an integer where 1 <= t <= 500, n is an integer where 2 <= n <= 100, and a is a list of n integers where 1 <= a_i <= 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: ntest is an input integer, t is an integer where 1 <= t <= 500, n is an integer where 2 <= n <= 100, a is a list of n integers where 1 <= a_i <= 10^9.
#Overall this is what the function does:The function `func` reads an integer `ntest` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers from the input. It sorts the list `a` and then prints the difference between the largest and smallest elements in the list. The function does not return any value. After the function concludes, the state of the program is that `ntest` test cases have been processed, and for each test case, the difference between the maximum and minimum elements of the list `a` has been printed.

