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
        
    #State of the program after the loop has been executed: Output State: `k`, `a`, `b`, and `v` are integers such that 2 ≤ k ≤ 1000, 1 ≤ a, b, v ≤ 1000; `res` is the number of iterations of the loop. After the loop finishes, `a` will be a non-negative integer, `b` will be less than `k`, and both `a` and `b` will be updated based on the initial values and loop conditions.
    print(res)
#Overall this is what the function does:The function `func` reads input integers `k`, `a`, `b`, and `v`, then iterates through a loop updating the values of `a` and `b` based on certain conditions until `a` reaches 0. The function keeps track of the number of iterations in `res` and prints the final value of `res`. The loop logic adjusts `a` and `b` based on the comparison with `k` and various conditions. There are potential edge cases where the loop may not terminate if the conditions are not met properly, leading to an infinite loop. Additionally, the function does not return any value, it only prints the result.

