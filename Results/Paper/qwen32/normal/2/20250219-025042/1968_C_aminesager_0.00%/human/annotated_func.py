#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 500, and x is a list of n-1 integers where each element x_i satisfies 1 <= x_i <= 500. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func():
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] - T[i - 1])
        
        a = a[::-1]
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: `t` is 0; `n` is an input integer greater than 1; `x` is a list of `n-1` integers where each element `x_i` satisfies `1 <= x_i <= 500`; `T` is a list of integers derived from the new input string `line` split and converted to integers; `a` is `[(1000 - sum(T[:n-1])), ..., (1000 - T[0]), 1000]`; `result` is a string that is the space-separated concatenation of the elements of `a`; `line` is the new input string provided by the user; `i` is `n-1`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n-1` integers. It then computes a list `a` of `n` integers based on the input list and prints this list as a space-separated string.

