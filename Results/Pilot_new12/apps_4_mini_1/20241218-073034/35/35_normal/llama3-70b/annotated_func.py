#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ a + b, a and b are integers such that 1 ≤ a, b ≤ 100.
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: When the loop finishes execution:
    #- The variables `n`, `a`, and `b` remain as integers in their original ranges.
    #- `x` will be the maximum feasible value satisfying the loop's exit conditions, which will be the largest number where the three conditions are still met (and it could reach 0 if those conditions are never satisfied).
    #
    #Output State:
    print(x)
#Overall this is what the function does:The function reads three integer inputs: `n`, `a`, and `b`. It determines the maximum value of `x` such that `x` is less than or equal to `n`, `a`, and `b`, and simultaneously satisfies the condition that `a` and `b` are both greater than or equal to `x` and that the sum of the remaining resources (`a - x + (b - x)`) is still at least `x`. If no such `x` exists, it can reduce down to 0. After executing, it prints the value of `x`, which could potentially be any integer from 0 to the minimum of the inputs. Notably, the function lacks direct error handling for inputs outside defined ranges, and there is an implicit assumption in the while loop that `x` starts no less than 0, which may not be guaranteed if inputs are not valid.

