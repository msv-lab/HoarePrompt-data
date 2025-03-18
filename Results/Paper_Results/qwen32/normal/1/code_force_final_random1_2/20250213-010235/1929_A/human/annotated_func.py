#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500; for each test case, n is an integer such that 2 ≤ n ≤ 100, and a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: `t` is an integer such that 1 ≤ t ≤ 500; `ntest` is greater than 0; `itest` equals `ntest`; no more test cases are processed; the loop has terminated.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the difference between the maximum and minimum values in the list `a`.

