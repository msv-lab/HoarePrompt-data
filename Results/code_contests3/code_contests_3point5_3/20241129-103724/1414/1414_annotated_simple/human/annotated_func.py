#State of the program right berfore the function call: k, a, b, v are integers such that 2 <= k <= 1000, 1 <= a, b, v <= 1000.**
def func():
    k, a, b, v = [int(x) for x in raw_input().split()]
    res = 0
    while a > 0:
        res += 1
        
        if b >= k:
            a = a - k * v
            b = b - (k - 1)
        elif b > 0:
            a = a - (b + 1) * v
            b = 0
        else:
            a = a - v
        
    #State of the program after the loop has been executed: `k`, `a`, `b`, `v`, `res` are integers such that 2 <= k <= 1000, 1 <= a, b, v <= 1000. After all iterations of the loop, `a` becomes less than or equal to 0, and `b` becomes 0. The final value of `res` depends on the number of times the loop executed and the conditions met during each iteration.
    print(res)
#Overall this is what the function does:The function `func` reads input for integers `k`, `a`, `b`, and `v`. It then iterates a loop based on the value of `a`, decrementing it according to certain conditions involving `b`, `k`, and `v`. The loop increments a counter `res` on each iteration. After the loop, it prints the final value of `res`. The function does not accept any parameters and does not return any value.

