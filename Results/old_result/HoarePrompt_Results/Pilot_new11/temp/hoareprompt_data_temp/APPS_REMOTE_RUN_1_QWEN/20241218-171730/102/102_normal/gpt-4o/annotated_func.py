#State of the program right berfore the function call: n, a, and b are integers such that 1 <= n, a, b <= 10 000 000.
def func_1():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        if (n - x * a) % b == 0:
            y = (n - x * a) // b
            print('YES')
            print(x, y)
            return
        
    #State of the program after the  for loop has been executed: Let's analyze the given loop step-by-step to determine the output state after all iterations of the loop have finished.
    #
    #### Initial State
    #- `n` is an integer obtained from input.
    #- `a` is an integer obtained from input.
    #- `b` is an integer obtained from input.
    #
    #### Loop Analysis
    #The loop runs for `x` in the range `n // a + 1`. For each iteration, it checks if \((n - x * a) \% b == 0\). If this condition is met, it sets \(y\) to \((n - x * a) // b\) and prints 'YES' followed by the values of \(x\) and \(y\), then returns. If the condition is not met, the loop continues to the next iteration.
    #
    #### Key Observations
    #1. **Loop Execution Condition**: The loop will only execute if \((n - x * a) \% b == 0\) is true for some \(x\) in the range \(0\) to \(n // a\).
    #2. **Return Statement**: The loop returns immediately when the condition is satisfied, so the loop can only execute once.
    #3. **No Further Iteration**: Once the loop finds a valid pair \((x, y)\), it exits without further iterations.
    #
    #### Output State After All Iterations
    #
    ##### Case 1: Loop Executes
    #- If the loop executes, it means there exists an integer \(x\) such that \((n - x * a) \% b == 0\). When this happens:
    #  - \(y = (n - x * a) // b\)
    #  - The function prints 'YES' and the values of \(x\) and \(y\)
    #  - The function returns
    #
    #Since the loop only executes once, the values of \(n\), \(a\), and \(b\) do not change.
    #
    ##### Case 2: Loop Does Not Execute
    #- If the loop does not execute, it means for all \(x\) in the range \(0\) to \(n // a\), the condition \((n - x * a) \% b == 0\) is false.
    #- In this case, the function does not print 'YES' or any values and simply returns without changing the values of \(n\), \(a\), and \(b\).
    #
    #### Final Output State
    #
    #- If the loop executes at least once, the function will have printed 'YES' and the values of \(x\) and \(y\), and returned. Hence, \(n\), \(a\), and \(b\) retain their original values.
    #- If the loop does not execute, the function simply returns without printing or changing the values of \(n\), \(a\), and \(b\).
    #
    #Thus, the final output state after all iterations of the loop have finished is:
    #
    #**Output State: **`n` is an integer obtained from input, `a` is an integer obtained from input, `b` is an integer obtained from input. The function will either print 'YES' along with the values of `x` and `y` and return, or it will return without any print statements and the values of `n`, `a`, and `b` remain unchanged.
    print('NO')
#Overall this is what the function does:The function `func_1` takes no parameters and returns `None`. It reads three integers `n`, `a`, and `b` from the standard input, where `1 <= n, a, b <= 10,000,000`. The function then iterates through a range determined by `n // a + 1` and checks if `(n - x * a) % b == 0` for each `x`. If such an `x` is found, it calculates `y = (n - x * a) // b`, prints 'YES' followed by the values of `x` and `y`, and returns. If no such `x` is found, the function prints 'NO' and returns. In all cases, the function ultimately returns `None`.

