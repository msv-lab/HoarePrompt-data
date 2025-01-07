#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ a, b ≤ 100 and 2 ≤ n ≤ a + b.
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: `n` is the original value of `n`, `a` is the original value of `a`, `b` is the original value of `b`, and `x` is the largest value for which `a >= x`, `b >= x`, and `a + b >= 3*x` are all true.
    print(x)
#Overall this is what the function does:The function calculates and prints the largest value `x` for which `a >= x`, `b >= x`, and `a + b - x >= x` are all true, given the initial conditions of `1 ≤ a, b ≤ 100` and `2 ≤ n ≤ a + b`, where `n`, `a`, and `b` are provided as input to the program. The function modifies no external state other than printing the calculated `x`, and the original values of `n`, `a`, and `b` remain unchanged throughout its execution. The loop iteratively decreases `x` until it finds the largest `x` that satisfies all conditions, handling potential edge cases where `x` might need to decrease to `1` or until it meets the specified conditions. The function does not handle invalid inputs explicitly, implying that it expects input validation to occur prior to its invocation, ensuring that the initial conditions are met.

