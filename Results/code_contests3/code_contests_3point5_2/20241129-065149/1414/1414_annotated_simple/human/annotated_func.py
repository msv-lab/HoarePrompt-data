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
        
    #State of the program after the loop has been executed: `k`, `a`, `b`, `v` hold integer values based on the input. `res` is equal to the number of iterations the loop executed. If the loop executed at least once, `a` will be less than or equal to 0, `b` will be less than or equal to 0, and `v` will be unchanged.
    print(res)
#Overall this is what the function does:The function `func` reads input values for k, a, b, and v, where k, a, b, and v are integers satisfying 2 ≤ k ≤ 1000, 1 ≤ a, b, v ≤ 1000. It then iterates a loop based on the values of a and b, calculating a result `res` that represents the number of iterations the loop executes. The function prints the final value of `res` after the loop finishes.

