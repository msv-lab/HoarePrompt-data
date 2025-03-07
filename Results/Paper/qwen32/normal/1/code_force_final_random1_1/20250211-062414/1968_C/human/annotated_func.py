#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 500, and x is a list of n-1 integers where each element x_i satisfies 1 <= x_i <= 500. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: After all iterations, `t` remains an integer such that 1 <= t <= 10^4. For each of the `t` test cases, `n` is an integer greater than 1, `x` is a list of `n-1` integers, and `a` is a list of `n` integers where `a[0]` is 1000 and each subsequent element `a[i]` is the cumulative sum starting from 1000 plus the sum of the elements in `x` up to `x[i-1]`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list `x` of `n-1` integers, then outputs a list `a` of `n` integers where the first element is 1000 and each subsequent element is the cumulative sum starting from 1000, incremented by the corresponding elements in `x`.

