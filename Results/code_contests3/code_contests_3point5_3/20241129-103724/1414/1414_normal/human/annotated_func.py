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
        
    #State of the program after the loop has been executed: After the loop has executed, `res` has been incremented by the number of times the loop ran. The final values of `a`, `b`, and `v` will depend on the initial values of `a`, `b`, and `v` as well as the conditions met within the loop.
    print(res)
#Overall this is what the function does:The function `func` reads input for integers `k`, `a`, `b`, and `v` within specified constraints, performs calculations inside a while loop based on conditions involving these input values, increments a counter `res` based on the number of loop iterations, and finally prints the value of `res`. It updates `a`, `b`, and `v` based on certain conditions within the loop, but it does not return any value.

