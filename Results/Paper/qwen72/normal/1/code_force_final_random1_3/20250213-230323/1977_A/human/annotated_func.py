#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n and m are integers such that 1 <= n, m <= 100.
def func():
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()]
        
        if n == m:
            print('Yes')
        elif m > n:
            print('No')
        elif m == n - 1:
            print('Yes')
        elif m % 2 == 0 and n % 2 == 0:
            print('Yes')
        elif m % 2 != 0 and n % 2 != 0:
            print('Yes')
        else:
            print('No')
        
    #State: After all iterations of the loop, `t` is an input integer between 1 and 100, inclusive, and must be greater than or equal to the number of iterations executed. `i` is equal to `t - 1`. For each iteration, `n` and `m` were integers read from the input. The conditions checked in the loop (whether `n` equals `m`, `m` is greater than `n`, `m` is `n - 1`, or the parity of `n` and `m`) were evaluated for each pair of `n` and `m` read from the input, and the corresponding output ('Yes' or 'No') was printed based on these conditions. The final state of `i` is `t - 1`, indicating that the loop has completed all its iterations. The values of `n` and `m` for each iteration are determined by the input provided and do not affect the final value of `i` or `t`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where `1 <= t <= 100`. For each test case, it reads two integers `n` and `m` (1 <= n, m <= 100) from the input. It then evaluates the following conditions for each pair of `n` and `m`:
- If `n` equals `m`, it prints 'Yes'.
- If `m` is greater than `n`, it prints 'No'.
- If `m` is `n - 1`, it prints 'Yes'.
- If both `m` and `n` are even, it prints 'Yes'.
- If both `m` and `n` are odd, it prints 'Yes'.
- Otherwise, it prints 'No'.
After processing all `t` test cases, the function completes, and the final state is that `t` test cases have been processed, and the appropriate output ('Yes' or 'No') has been printed for each test case.

