#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 500, and x_2, ..., x_n are integers such that 1 ≤ x_i ≤ 500.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: _ is t-1, `n` is a positive integer (at least 1), `x` is a list of integers derived from user input, `a` is a list of length `n` initialized to `[0] * n` with `a[0]` set to 1000, and for each index `i` from 1 to `n-1`, `a[i]` is `a[i-1] + x[i-1]`.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list of integers `x`. It then generates a new list `a` of length `n`, where the first element is always 1000, and each subsequent element is the sum of the previous element in `a` and the corresponding element in `x`. The function prints the list `a` for each test case. After processing all test cases, the function completes without returning any value.

