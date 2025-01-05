#State of the program right berfore the function call: k, a, b, and v are integers such that 2 <= k <= 1000, 1 <= a, b, v <= 1000.**
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
        
    #State of the program after the loop has been executed: `k`, `a`, `b`, and `v` are integers within the specified ranges; `res` is the number of times the loop executed. If `b >= k`, `b` is updated accordingly. If `b > 0`, `a` is updated based on the provided formulas and `b` is set to 0. If `b <= 0`, `a` is decremented by `v`. In the end, `a` is less than or equal to 0.
    print(res)
#Overall this is what the function does:The function `func` reads input values for variables `k`, `a`, `b`, and `v` which are integers within specific ranges. It then enters a loop that decrements `a` based on conditions involving `k`, `b`, and `v`. The loop increments a counter `res` until `a` becomes less than or equal to 0. The function does not explicitly return any value but prints the final value of `res`.

