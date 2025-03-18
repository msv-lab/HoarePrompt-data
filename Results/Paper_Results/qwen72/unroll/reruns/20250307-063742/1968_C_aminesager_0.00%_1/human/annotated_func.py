#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 2 <= n <= 500, and x is a list of n-1 integers where 1 <= x_i <= 500. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: t = 0, n is unchanged, x is unchanged, and a is a list of n integers where each element is the result of subtracting the corresponding element from the input list T from the previous element in the list a, starting with 1000. The list a is then reversed and printed as a space-separated string.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a space-separated list of `n-1` integers `T`. It then computes a list `a` of `n` integers where each element is derived by subtracting the corresponding element from `T` from the previous element in `a`, starting with 1000. The list `a` is reversed and printed as a space-separated string. After processing all test cases, `t` is 0, and the function concludes. The function does not return any value.

