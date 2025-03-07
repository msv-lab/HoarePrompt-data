#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: `t` is an integer such that 1 ≤ t ≤ 500; `ntest` is equal to `itest + 1`, indicating that all test cases have been processed; `itest` is equal to `ntest - 1`, representing the last iteration of the loop. The variables `n` and `a` hold the values from the last test case processed, with `a` being a sorted list of `n` integers where each integer `a_i` satisfies 1 ≤ a_i ≤ 10^9.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the difference between the maximum and minimum integers in the list `a`.

