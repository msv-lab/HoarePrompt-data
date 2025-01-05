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
        
    #State of the program after the loop has been executed: After the loop finishes executing, `k`, `a`, `b`, `v` are integers within the specified ranges. The final value of `res` will be the number of times the loop executed successfully. The final values of `a` and `b` may have been updated based on the conditions within the loop.
    print(res)
#Overall this is what the function does:Functionality: The function `func` reads input integers `k`, `a`, `b`, and `v` from the user. It then iterates a loop based on the value of `a` and updates the variables `a` and `b` according to certain conditions. The final value of `res` represents the number of successful loop iterations. The function does not explicitly return a value, but it prints the final value of `res` after the loop completes. This function lacks explicit return statements and does not cover edge cases where `a`, `b`, or `v` fall outside the specified ranges.

