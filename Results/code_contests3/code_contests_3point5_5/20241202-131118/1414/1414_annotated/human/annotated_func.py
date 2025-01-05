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
        
    #State of the program after the loop has been executed: `k`, `a`, `b`, and `v` are integers such that 2 ≤ k ≤ 1000, 1 ≤ a, b, v ≤ 1000; `res` is incremented by 1 for each iteration of the loop. Upon completion of all iterations, `a` is less than or equal to 0, and `b` is equal to 0 or negative.
    print(res)
#Overall this is what the function does:The function `func` reads four integers from the input, `k`, `a`, `b`, and `v`, and then iterates a loop based on the value of `a`. During each iteration, `res` is incremented by 1. Depending on the conditions within the loop, the values of `a` and `b` are updated accordingly. Once the loop finishes, the function prints the final value of `res`. The function does not explicitly return any value.

