#State of the program right berfore the function call: h is an integer such that 1 ≤ h ≤ 50, and n is an integer such that 1 ≤ n ≤ 2^h.
def func():
    h, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            ans += n // 2 - 1
        else:
            ans += n // 2
        
        n //= 2
        
    #State of the program after the loop has been executed: `n` is 1, `ans` is the total accumulated from the initial value of `n` based on its even or odd nature during the iterations.
    print(ans)
#Overall this is what the function does:The function accepts two integers, `h` and `n`, where `1 ≤ h ≤ 50` and `1 ≤ n ≤ 2^h`. It calculates a value `ans` based on the iterations of halving `n` until it becomes 1. During each iteration, if `n` is even, it adds `(n // 2 - 1)` to `ans`; if `n` is odd, it adds `(n // 2)` to `ans`. Finally, it prints the accumulated value `ans`. The function does not return any value.

