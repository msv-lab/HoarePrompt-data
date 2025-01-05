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
        
    #State of the program after the loop has been executed: `k`, `a`, `b`, and `v` are input integers, `res` is the number of times the loop executed successfully. After all iterations, `a` is less than or equal to 0, `b` is less than `k`, `v` remains the same.
    print(res)
#Overall this is what the function does:The function `func` reads input integers `k`, `a`, `b`, and `v` from the user, where 2 <= k <= 1000 and 1 <= a, b, v <= 1000. It then iterates a while loop based on the value of `a`, incrementing `res` each time. Within the loop, it updates the values of `a` and `b` based on certain conditions involving `k` and `v`. After the loop, it prints the final value of `res`. The function does not have a return value.

