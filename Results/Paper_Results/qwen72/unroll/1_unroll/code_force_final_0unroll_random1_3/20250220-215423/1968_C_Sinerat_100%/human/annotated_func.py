#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where each x_i satisfies 1 ≤ x_i ≤ 500.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where each x_i satisfies 1 ≤ x_i ≤ 500. a is a list of n integers where a[0] = 1000 and for each i from 1 to n-1, a[i] = a[i-1] + x[i-1].
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `x` of `n-1` integers. It then constructs a new list `a` of `n` integers where `a[0]` is always 1000, and each subsequent element `a[i]` (for `1 ≤ i ≤ n-1`) is the sum of the previous element `a[i-1]` and the corresponding element `x[i-1]`. The function prints the elements of the list `a` for each test case. After the function concludes, the state of the program is that `t` test cases have been processed, and for each test case, a list `a` of `n` integers has been printed, where `a[0] = 1000` and `a[i] = a[i-1] + x[i-1]` for `1 ≤ i ≤ n-1`.

