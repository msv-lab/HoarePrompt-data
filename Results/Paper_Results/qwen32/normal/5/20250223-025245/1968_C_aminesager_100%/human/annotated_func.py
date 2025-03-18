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
            a.append(a[i - 1] + T[i - 1])
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: `t` is 0.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list `x` of `n-1` integers. For each test case, it calculates a new list `a` such that each element `a[i]` is the sum of the previous element `a[i-1]` and the corresponding element `x[i-1]` from the input list, starting with `a[0]` initialized to 1000. It then prints the resulting list `a` for each test case.

