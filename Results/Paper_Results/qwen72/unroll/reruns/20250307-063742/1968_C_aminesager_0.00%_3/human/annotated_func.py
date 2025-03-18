#State of the program right berfore the function call: The function should take a list of integers `x` as input, where `x` has a length of `n-1` and each element `x_i` satisfies 1 ≤ x_i ≤ 500. The function should also handle multiple test cases, indicated by an integer `t` (1 ≤ t ≤ 10^4). For each test case, the length `n` of the array `a` must satisfy 2 ≤ n ≤ 500, and the sum of all `n` values across test cases should not exceed 2 · 10^5.
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
        
    #State: The value of `t` is 0, and the list `a` contains the computed values for each test case, which are printed in reverse order as a space-separated string. The initial list `x` remains unchanged as it is not modified within the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of integers `T` of length `n-1`, where each element `T_i` satisfies 1 ≤ T_i ≤ 500. It then computes a new list `a` of length `n` such that `a[i] = a[i-1] - T[i-1]` for `1 ≤ i < n`, starting with `a[0] = 1000`. The list `a` is reversed and printed as a space-separated string. After processing all test cases, the value of `t` is 0, and the function does not return any value. The function does not modify any input parameters.

