#State of the program right berfore the function call: n and k are integers where 1 ≤ n ≤ 3 · 10^5 and 1 ≤ k ≤ 2 · 10^9. a is a list of n integers where 1 ≤ a_i ≤ 10^9. b is a list of length n + 1 initialized to 0.
def func_1():
    try:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = [0] * (n + 1)
        for i in range(n):
            x = int(input())
            
            b[abs(x)] += a[i]
            
        #State: After the loop executes all the iterations, `n` remains unchanged, `i` is `n-1`, `x` is the last input integer, and for each index `j` in the range from 0 to `n`, `b[j]` is incremented by the sum of `a[i]` for all `i` such that `abs(int(input())) == j`.
        r = 0
        for i in range(1, n + 1):
            r += k
            
            if r < b[i]:
                print('NO')
                return
            
            r -= b[i]
            
        #State: After the loop executes all iterations, `n` remains unchanged, `i` is `n-1`, `x` is the last input integer, `b` is an array where each element `b[j]` is incremented by the sum of `a[i]` for all `i` such that `abs(int(input())) == j` for each `j` in the range from 0 to `n`, and `r` is `k * n - sum(b[1:n])`, with `r` being greater than or equal to each `b[i]` for `i` in the range from 1 to `n`. If at any point `r` is less than `b[i]`, the program prints 'NO' and returns without completing the loop.
        print('YES')
        #This is printed: YES
    except (ValueError):
        print('Invalid input format')
        #This is printed: Invalid input format
    #State: If the input format is valid, `n` and `k` remain unchanged, `a` is a list of `n` integers, `b` is a list of length `n + 1` where each element `b[j]` is incremented by the sum of `a[i]` for all `i` such that `abs(int(input())) == j`, and `r` is `k * n - sum(b[1:n])`. If at any point `r` is less than `b[i]`, the program prints 'NO' and returns without completing the loop. If the loop completes, the program prints 'YES'. If a `ValueError` occurs, the program prints 'Invalid input format' and returns.
#Overall this is what the function does:The function `func_1` reads input values for `n` and `k`, followed by a list `a` of `n` integers, and then `n` additional integers. It processes these inputs to update a list `b` of length `n + 1` based on the absolute values of the additional integers. The function checks if a certain condition involving `k` and the updated list `b` is met. If the condition fails at any point, the function prints 'NO' and exits. If the condition holds for all elements, the function prints 'YES'. In case of invalid input, the function prints 'Invalid input format'. The function does not return any value.

#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 3 · 10^4.
def func_2():
    try:
        t = int(input())
        for _ in range(t):
            func_1()
            
        #State: `t` is an input integer such that 1 ≤ t ≤ 3 · 10^4, `_` is t-1.
    except (ValueError):
        print('Invalid input format')
        #This is printed: Invalid input format
    #State: If the input is a valid integer within the range 1 ≤ t ≤ 3 · 10^4, `t` is set to this integer, and the function `func_1()` is called `t` times. If the input is not a valid integer, the program prints "Invalid input format" and does not execute the loop or call `func_1()`.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the user input, where `t` is expected to be within the range 1 ≤ t ≤ 3 · 10^4. If the input is a valid integer within this range, the function calls another function `func_1` exactly `t` times. If the input is not a valid integer or is outside the specified range, the function prints "Invalid input format" and does not execute the loop or call `func_1`. The function does not return any value.

