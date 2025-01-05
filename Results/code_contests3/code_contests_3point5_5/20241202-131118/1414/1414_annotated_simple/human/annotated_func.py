#State of the program right berfore the function call: **Precondition**: **k, a, b, v are integers such that 2 <= k <= 1000, 1 <= a, b, v <= 1000.**
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
        
    #State of the program after the loop has been executed: `k`, `a`, `b`, `v` are integers within the specified range. `res` is the number of times the loop executed. At the end of the loop, `a` will be a non-positive integer, `b` will be 0 or less, and `res` will be the total number of times the loop executed.
    print(res)
#Overall this is what the function does:The function `func` reads four integers `k`, `a`, `b`, and `v` from input, and then iterates a loop based on the values of `a` and `b`. The loop increments a counter `res` with each iteration. Depending on the conditions within the loop, the values of `a` and `b` are updated. At the end, the function prints the final value of `res`. The function operates under the constraint that `k`, `a`, `b`, and `v` are integers within the ranges 2 <= k <= 1000, 1 <= a, b, v <= 1000. It does not have a return value specified.

