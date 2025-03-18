#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers such that 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
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
        
    #State: The list `a` contains `n` elements where each element `a[j]` (for `j` from 0 to `n-1`) is equal to the sum of the first `j+1` elements of `T` plus `a[0] + T[0]`. The variable `t` is 0, indicating that the loop has completed all its iterations. The variable `result` is a space-separated string containing the elements of `a`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t`, an integer `n`, and a list `x` of `n-1` integers. It then computes a list `a` where each element `a[j]` (for `j` from 0 to `n-1`) is the sum of the first `j+1` elements of `x` plus the initial value `a[0] + x[0]`. Finally, it prints a space-separated string containing the elements of `a`. After processing all test cases, the function concludes with `t` set to 0, indicating all iterations are complete.

