#State of the program right berfore the function call: The function `func` should take an integer `t` as the number of test cases, and for each test case, an integer `n` and a list of integers `x` where `2 <= n <= 500` and `1 <= x_i <= 500` for all `2 <= i <= n`. The sum of values `n` over all test cases does not exceed `2 * 10^5`.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: For each test case, the output state is a list `a` of length `n` where `a[0]` is 500 and `a[i]` for `1 <= i < n` is the cumulative sum of the elements in `x` starting from `x[0]` up to `x[i-1]`, added to 500.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list of integers `x` from user input. It then generates a list `a` of length `n` where `a[0]` is always 500, and for each subsequent index `i` (1 ≤ i < n), `a[i]` is the cumulative sum of the elements in `x` from `x[0]` to `x[i-1]`, added to 500. The function prints the list `a` for each test case.

