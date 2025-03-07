#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where each element x_i satisfies 1 ≤ x_i ≤ 500. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is 0; no further iterations occur; the final `result` printed for each iteration is a space-separated string of `n` integers where each integer is calculated as 1000 minus the cumulative sum of the first (i-1) elements of `T`, in reverse order.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n-1` integers. For each test case, it calculates a list of `n` integers where each integer is derived by subtracting the cumulative sum of the previous elements from 1000, in reverse order. It then prints this list as a space-separated string.

