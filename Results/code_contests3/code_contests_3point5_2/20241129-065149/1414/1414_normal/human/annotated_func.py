#State of the program right berfore the function call: k, a, b, and v are integers such that 2 ≤ k ≤ 1000, 1 ≤ a, b, v ≤ 1000.**
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
        
    #State of the program after the loop has been executed: Output State: `res` is the number of times the loop executed successfully, `a` is an integer greater than 0. If `b >= k`, `a` is updated by subtracting `k * v` and `b` is updated by subtracting `(k - 1)`. If `b < k`, `a` is updated based on the calculation of `(b + 1) * v` and `b` becomes 0. If `b <= 0`, `a` is updated by subtracting `v`. The final values of `a` and `b` depend on the conditions met during the loop execution.
    print(res)
#Overall this is what the function does:The function `func()` reads four integers from the input, denoted as k, a, b, and v, within the specified ranges. It then iterates a loop based on the value of a with different conditions. The loop increments a counter `res` by 1 for each iteration. Depending on the values of a, b, and k, the loop updates the values of a and b accordingly. The final values of a and b are dependent on the conditions met during the loop execution. At the end, the function prints the value of `res`. The function does not explicitly return any value.

