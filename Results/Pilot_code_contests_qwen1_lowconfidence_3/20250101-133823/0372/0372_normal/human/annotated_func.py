#State of the program right berfore the function call: n is an integer such that 3 <= n <= 1000.
def func():
    n = int(raw_input())
    for i in range(n / 2):
        if gcd(n - i, i) == 1:
            print(str(i) + ' ' + str(n - i))
        
    #State of the program after the  for loop has been executed: To determine the output state after all iterations of the loop have finished, let's analyze the loop code and the conditions under which the loop operates.
    #
    #### Analysis of the Loop Code
    #The loop iterates over `i` from `0` to `n/2 - 1`. For each iteration, it checks if the greatest common divisor (gcd) of `n - i` and `i` is 1. If it is, it prints `i` and `n - i`.
    #
    #### Initial Conditions
    #- `n` is an integer such that \(3 \leq n \leq 1000\).
    #- The loop starts with `i = 0` and increments `i` by 1 in each iteration until `i` reaches `n/2`.
    #
    #### Iterations and Conditions
    #1. **First Iteration (i = 0):**
    #   - Check `gcd(n - 0, 0) = gcd(n, 0)`, which is always 0. No output.
    #   
    #2. **Second Iteration (i = 1):**
    #   - Check `gcd(n - 1, 1) = gcd(n - 1, 1)`, which is 1 if and only if `n - 1` is coprime with 1. Always true, so print `1` and `n - 1`.
    #
    #3. **Third Iteration (i = 2):**
    #   - Check `gcd(n - 2, 2)`. This will depend on the value of `n`. If `n - 2` is odd, then `gcd(n - 2, 2) = 1` and it will print `2` and `n - 2`.
    #
    #4. **General Iteration (i = k):**
    #   - The loop continues to check `gcd(n - k, k)` and prints `k` and `n - k` if the gcd is 1.
    #
    #### Final Iteration and Termination
    #- The loop terminates when `i` reaches `n/2`.
    #- During the loop, the loop prints pairs `(i, n - i)` where `gcd(i, n - i) = 1`.
    #
    #### Conclusion
    #After all iterations, the loop will have printed all pairs `(i, n - i)` such that `0 < i < n/2` and `gcd(i, n - i) = 1`.
    #
    #### Output State
    #- The value of `n` remains unchanged and is still within the range \(3 \leq n \leq 1000\).
    #- The value of `i` after the loop finishes is `n/2` (since the loop runs from `0` to `n/2 - 1` and then stops).
    #
    #Thus, the output state after all iterations of the loop have finished is:
    #
    #**Output State: **`n` is an integer in the range 3 to 1000, `i` is `n/2`. All pairs `(i, n - i)` such that `0 < i < n/2` and `gcd(i, n - i) = 1` have been printed.
#Overall this is what the function does:The function `func()` takes no parameters and operates on an integer `n` where \(3 \leq n \leq 1000\). It prints all pairs \((i, n - i)\) such that \(0 < i < n/2\) and the greatest common divisor (gcd) of \(i\) and \(n - i\) is 1. After executing the loop, the variable `n` remains unchanged, and the variable `i` will be set to `n/2`.

