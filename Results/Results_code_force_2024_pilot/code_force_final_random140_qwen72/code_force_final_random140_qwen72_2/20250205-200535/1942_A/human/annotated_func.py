#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^3, and for each test case, n and k are integers where 1 ≤ k ≤ n ≤ 10^3.
def func():
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        elif k == 1:
            print(' '.join([str(x + 1) for x in range(n)]))
        else:
            print(-1)
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^3, `n` and `k` are integers read from input where 1 ≤ k ≤ n ≤ 10^3, `_` is `t-1`. The loop has executed `t` times, and for each iteration, the conditions within the loop were evaluated based on the values of `n` and `k` provided for that specific test case. If `n` was equal to `k`, the output was a sequence of `1`s repeated `n` times. If `k` was 1, the output was a sequence of integers from 1 to `n`. If neither condition was met, the output was `-1`. The values of `t`, `n`, and `k` for each test case remain as they were initially provided, and the loop variable `_` has reached its final value of `t-1`.
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of two integers `n` and `k`. It processes each test case and prints a specific output based on the values of `n` and `k`. If `n` equals `k`, it prints a sequence of `1`s repeated `n` times. If `k` is 1, it prints a sequence of integers from 1 to `n`. If neither condition is met, it prints `-1`. After processing all test cases, the function completes without returning any value. The state of the program remains unchanged except for the printed outputs.

