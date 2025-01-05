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
        
    #State of the program after the loop has been executed: `k`, `a`, `b`, `v` are integers such that 2 <= k <= 1000, 1 <= a, b, v <= 1000; `res` is the number of iterations the loop has executed. If a > 0, then `a` is updated based on the conditions inside the loop. If b >= k, `a` is updated to `a - k * v` and `b` changes. If b < k and b > 0, `a` is updated to `a - (b + 1) * v` and `b` becomes 0. If b <= 0, `a` is decreased by `v`. The loop stops when `a` becomes less than or equal to 0.
    print(res)
#Overall this is what the function does:Functionality: The function `func` reads input values for `k`, `a`, `b`, and `v`, where `k`, `a`, `b`, and `v` are integers satisfying 2 <= k <= 1000 and 1 <= a, b, v <= 1000. It then enters a loop where it iterates and updates `a` and `b` based on certain conditions until `a` becomes less than or equal to 0. The number of iterations is stored in `res` and then printed. The function does not have a return value specified.

