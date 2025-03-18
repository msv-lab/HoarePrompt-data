#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ a + b, a is an integer representing the number of pieces of the first cake where 1 ≤ a ≤ 100, and b is an integer representing the number of pieces of the second cake where 1 ≤ b ≤ 100.
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: To determine the output state after the loop has executed all necessary times, consider that the loop continues decrementing `x` until the condition `a >= x` and `b >= x` and `a - x + (b - x) >= x` is satisfied.
    #
    #**Output State:**
    #`x` is equal to `min(n, a, b) - k` where `k` is the number of times the loop executed until the condition was satisfied, `a - (min(n, a, b) - k) + (b - (min(n, a, b) - k)) >= (min(n, a, b) - k)` must remain true for all k iterations; `n` is an integer satisfying `1 ≤ n ≤ a + b`, `a` is an integer satisfying `1 ≤ a ≤ 100`, `b` is an integer satisfying `1 ≤ b ≤ 100`. `x` must satisfy `x ≥ 0` upon loop termination.
    print(x)
#Overall this is what the function does:The function reads three integers: `n`, `a`, and `b`, where `1 ≤ n ≤ a + b`, `1 ≤ a ≤ 100`, and `1 ≤ b ≤ 100`. It calculates the largest integer `x` such that `x <= min(n, a, b)` and ensures that `a` and `b` can collectively provide enough pieces to satisfy the condition `a >= x`, `b >= x`, and `a - x + (b - x) >= x`. If the initial value of `x` does not meet these conditions, the function decrementally adjusts `x` until a valid state is achieved or until `x` becomes less than zero. Finally, the function prints the calculated value of `x`, which may be `0` if no valid configuration exists within the constraints. Thus, the function outputs the maximum number of pieces of cake that can be evenly distributed, taking into account the given constraints and limitations.

