#State of the program right berfore the function call: the input is an integer n such that 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: To determine the output state of the loop after all iterations have finished, let's analyze the loop code and the given output states for the first few iterations.
    #
    #The loop code is:
    #```python
    #for i in range(1, int(n ** 0.5) + 1):
    #    if n % i == 0:
    #        res += 2
    #    if i * i == n:
    #        res -= 1
    #```
    #From the given output states, we can observe the following patterns:
    #
    #- The loop will execute at least once if `n` is an integer greater than or equal to 1.
    #- If `n` is 1, `res` will be 1 after the first iteration because `n` is a square of `i` and `n` is a multiple of `i`.
    #- If `n` is not 1 but is a multiple of `i`, `res` will be incremented by 2 for each multiple found.
    #- If `n` is a perfect square (i.e., `i * i == n`), `res` will be decremented by 1 after being incremented by 2, effectively incrementing `res` by 1 for that `i`.
    #
    #Let's break down the loop's behavior:
    #
    #1. **Loop Execution Condition**: The loop will run for `i` values from 1 to the square root of `n` (inclusive). This means the loop will execute at least once if `n` is 1 or more, because the range will include at least the value 1.
    #
    #2. **Update of `res`**:
    #    - For every `i` where `n` is divisible by `i`, `res` is incremented by 2. This counts both `i` and its corresponding factor `n/i` as divisors of `n`, except when `i` equals `n/i` (which happens when `n` is a perfect square).
    #    - If `n` is a perfect square, the condition `i * i == n` will be true for the `i` that is the square root of `n`. In this case, after incrementing `res` by 2 (for the square root and itself), it then decrements `res` by 1 to avoid double-counting the square root.
    #
    #3. **Final State of `res`**:
    #    - If `n` is not a perfect square, `res` will be twice the number of divisors of `n` that are less than or equal to the square root of `n`, because each divisor `i` has a corresponding divisor `n/i`, and these pairs are counted together.
    #    - If `n` is a perfect square, `res` will be twice the number of divisors less than the square root of `n`, plus one for the square root itself (since it doesn't have a separate pair).
    #
    #4. **Edge Case**: If `n` is less than 1, the loop will not execute, and `res` will remain 0, reflecting that there are no divisors to count in this scenario.
    #
    #Given these observations, the output state after all iterations of the loop have finished can be generalized as follows:
    #
    #- `n` retains its original value as it's not modified within the loop.
    #- `res` equals the total number of divisors of `n`, considering that each pair of divisors (`i` and `n/i`) contributes 2 to `res`, except when `n` is a perfect square, in which case its square root contributes 1.
    #
    #**Output State: `n` is an integer, `res` is the total number of divisors of `n`.**
    print(res)
#Overall this is what the function does:The function calculates and returns the total number of divisors of a given integer `n`, where `n` is an integer greater than or equal to 1 and less than or equal to 10^9. The function first takes an integer input from the user, then iterates through all numbers from 1 to the square root of `n` to find its divisors. For each divisor found, it increments a counter `res` by 2, except when `n` is a perfect square, in which case it decrements `res` by 1 after the increment to avoid double-counting the square root. The function handles edge cases such as `n` being 1 (in which case it has only 1 divisor) and perfect squares, where the square root is counted only once. After executing the loop, the function prints the total number of divisors found, stored in `res`. The state of the program after the function concludes includes the user-inputted integer `n` and the calculated total number of divisors of `n`, which is printed as output.

