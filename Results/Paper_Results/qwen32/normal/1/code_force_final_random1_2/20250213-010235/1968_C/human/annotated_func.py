#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where each element x_i satisfies 1 ≤ x_i ≤ 500. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: t is 0, n and x are the values from the last test case, and a is the array computed for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `x` of `n-1` integers. For each test case, it computes and prints a list `a` of length `n`, where each element is determined by accumulating the values from `x` starting from an initial value of 1000.

