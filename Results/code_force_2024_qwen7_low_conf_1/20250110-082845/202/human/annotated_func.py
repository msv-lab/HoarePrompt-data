#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and s is a binary string of length n.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        mn = 0
        
        mx = 0
        
        cur = 0
        
        for c in s:
            if (cur % 2 == 0) == (c == '1'):
                cur = cur + 1
            else:
                cur = cur - 1
            mn = min(mn, cur)
            mx = max(mx, cur)
        
        print(mx - mn)
        
    #State of the program after the  for loop has been executed: Let's analyze the loop step-by-step based on the provided code and initial conditions.
    #
    #### Initial State
    #- `t` is an integer between 1 and \(10^4\) (inclusive).
    #- `n` is a positive integer such that \(1 \leq n \leq 2 \cdot 10^5\).
    #- `s` is a binary string of length `n`.
    #
    #### Loop Code Analysis
    #```python
    #for _ in range(t):
    #    n = int(input())  # User inputs `n`
    #    s = input()       # User inputs `s` (a binary string of length `n`)
    #    mn = 0            # Initialize `mn` to 0
    #    mx = 0            # Initialize `mx` to 0
    #    cur = 0           # Initialize `cur` to 0
    #    for c in s:       # Iterate over each character in `s`
    #        if (cur % 2 == 0) == (c == '1'):
    #            cur = cur + 1
    #        else:
    #            cur = cur - 1
    #        mn = min(mn, cur)  # Update `mn` to the minimum value of `cur`
    #        mx = max(mx, cur)  # Update `mx` to the maximum value of `cur`
    #    print(mx - mn)     # Print the difference `mx - mn`
    #```
    #
    #### Step-by-Step Analysis
    #1. **Loop Execution Summary:**
    #   - For each iteration of the outer loop (`_ in range(t)`), the inner loop processes the string `s`.
    #   - The variable `cur` keeps track of the parity (even/odd) changes based on the input string `s`.
    #   - The variables `mn` and `mx` record the minimum and maximum values of `cur` during the processing of `s`.
    #
    #2. **Final Values After All Iterations:**
    #   - Since the loop iterates `t` times, `t` different strings `s` are processed.
    #   - After processing all `t` strings, `mn` will be the minimum value of `cur` across all strings.
    #   - Similarly, `mx` will be the maximum value of `cur` across all strings.
    #   - `cur` will be the final value of `cur` after processing the last string `s`.
    #
    #3. **Output State After All Iterations:**
    #   - The loop will execute exactly `t` times, and for each iteration, `mn`, `mx`, and `cur` will be updated accordingly.
    #   - The value printed will be `mx - mn`, which represents the range of `cur` values across all processed strings.
    #
    #### Final Output State
    #After all iterations of the loop, the following will hold true:
    #- `t` is the number of times the outer loop has executed.
    #- `mn` is the minimum value that `cur` took across all iterations.
    #- `mx` is the maximum value that `cur` took across all iterations.
    #- `cur` is the final value of `cur` after processing the last string `s`.
    #
    #**Output State:**
    #```plaintext
    #Output State: t is the number of times the outer loop has executed, mn is the minimum value that cur took across all iterations, mx is the maximum value that cur took across all iterations, cur is the final value of cur after processing the last string s.
    #```
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a positive integer `n` and a binary string `s` of length `n`. It then calculates the range of values that a counter `cur` takes, starting from 0, while iterating over the characters of `s`. The counter `cur` increments by 1 if the current character and the previous value of `cur` have the same parity (both even or both odd), and decrements by 1 otherwise. The function keeps track of the minimum and maximum values of `cur` across all test cases. Finally, it prints the difference between the maximum and minimum values of `cur` for each test case.

