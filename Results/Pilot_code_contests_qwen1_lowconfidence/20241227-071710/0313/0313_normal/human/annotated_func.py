#State of the program right berfore the function call: a and c are non-negative integers such that 0 ≤ a, c ≤ 10^9.
def func():
    ans = 0
    a, b = [int(x) for x in sys.stdin.readline().strip().split()]
    while a > 0 and b > 0:
        ans *= 3
        
        ans += (3 - a % 3 + b % 3) % 3
        
        a //= 3
        
        b //= 3
        
    #State of the program after the loop has been executed: `a` is 0, `b` is 0, `ans` is calculated as follows: if the initial values of `a` and `b` were both greater than 0, `ans` contains a specific transformation based on the sum and modulus operations performed on `a` and `b`. If either `a` or `b` was initially 0, the loop may not have executed at all, and `ans` would still be 0.
    print(ans)
#Overall this is what the function does:The function reads two non-negative integers `a` and `b` from standard input, where \(0 \leq a, b \leq 10^9\). It then iteratively transforms these integers using specific arithmetic operations until both `a` and `b` become zero. During each iteration, `ans` is updated based on the modulo and sum operations of `a` and `b`. After the loop completes, the function prints the final value of `ans`. The function does not return a value explicitly, but the final state of `ans` is the output. Edge cases include when either `a` or `b` is initially zero; in such cases, the loop may not execute at all, and `ans` remains zero.

