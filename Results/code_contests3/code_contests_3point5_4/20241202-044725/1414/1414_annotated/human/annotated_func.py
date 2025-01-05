#State of the program right berfore the function call: k, a, b, and v are all integers such that 2 <= k <= 1000, 1 <= a, b, v <= 1000.**
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
        
    #State of the program after the loop has been executed: `k`, `a`, `b`, and `v` are integers satisfying 2 <= k <= 1000, 1 <= a, b, v <= 1000; `res` is increased by the total number of times the loop executed. After the loop has finished, `a` will be less than or equal to 0, and `b` will be 0.
    print(res)
#Overall this is what the function does:The function `func` reads input integers `k`, `a`, `b`, and `v` from the user. It then calculates a result based on these inputs by decrementing `a` according to certain conditions in a loop. The loop updates `res` based on the number of iterations. After the loop finishes, `res` is printed. The functionality of the function is to perform a calculation using the input integer values `k`, `a`, `b`, and `v` and output the final result as `res`.

