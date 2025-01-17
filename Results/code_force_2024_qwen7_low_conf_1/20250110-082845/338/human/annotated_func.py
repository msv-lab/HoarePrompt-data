#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, n, m, and k are positive integers such that 1 ≤ m, k ≤ n ≤ 50 for each test case.
def func_1(n, m, k):
    if (m == k or k > n) :
        return 'NO'
        #The program returns 'NO'
    else :
        if (m > k) :
            return 'YES'
            #The program returns 'YES'
        else :
            return 'NO'
            #The program returns 'NO'
#Overall this is what the function does:- The function does not handle cases where `n`, `m`, or `k` are outside their specified ranges (1 ≤ m, k ≤ n ≤ 50). If such inputs are given, the function will still execute based on the provided conditions but will not enforce these constraints.

