#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ a + b, where a and b are integers such that 1 ≤ a, b ≤ 100.
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: `x` is the maximum value such that `a >= x` and `b >= x` and `a - x + (b - x) >= x`, `n` is an integer such that `2 ≤ n ≤ a + b`, `a` is an integer between 1 and 100, `b` is an integer between 1 and 100. If the loop executed zero times, the original `x` was `min(n, a, b)`.
    print(x)
#Overall this is what the function does:The function accepts three integers `n`, `a`, and `b` from user input, and calculates the maximum value of `x` such that `x` is less than or equal to both `a` and `b`, and the remaining amounts can together satisfy `x`. It prints this value of `x`, with the understanding that it should not allow `x` to become negative due to the constraints provided.

