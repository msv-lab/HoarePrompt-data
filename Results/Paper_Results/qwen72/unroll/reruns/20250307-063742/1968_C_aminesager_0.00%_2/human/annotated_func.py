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
        
    #State: t is 0, n is the last input integer, x is unchanged, and the last computed list a is printed in reverse order.
#Overall this is what the function does:The function `func` reads input values for `t` test cases. For each test case, it reads an integer `n` and a list of `n-1` integers `T`. It then computes a list `a` of `n` integers in reverse order, where each element is derived by subtracting the corresponding element from `T` from the previous element in `a`. The function prints the computed list `a` for each test case. After processing all test cases, `t` is 0, `n` is the last input integer, and the list `a` is printed in reverse order. The function does not return any value.

