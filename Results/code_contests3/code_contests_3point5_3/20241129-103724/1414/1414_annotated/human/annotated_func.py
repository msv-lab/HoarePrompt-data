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
        
    #State of the program after the loop has been executed: `res` is the number of times the loop executed, `a` is greater than 0, `b` is either 0 or less than 0, loop has ended
    print(res)
#Overall this is what the function does:The function `func` reads input from the user consisting of four integers `k`, `a`, `b`, and `v` within specified constraints. It then enters a loop where it increments `res` by 1 for each iteration. Depending on the values of `b` and `k`, it adjusts the values of `a` and `b` accordingly. The loop continues until `a` becomes less than or equal to 0. The function does not return any value but prints the final value of `res`, which represents the number of iterations executed.

