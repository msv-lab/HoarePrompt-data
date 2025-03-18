#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer, such that 1 <= n <= 1000 and 0 <= k <= 1000.
def func():
    n, k = map(int, input().split())
    l = (n + k - 1) // (k * 2 + 1)
    res = []
    for i in range(l):
        res.append(i * (k * 2 + 1) + 1)
        
    #State of the program after the  for loop has been executed: To determine the output state after all iterations of the loop have finished, let's analyze the given information and the loop code.
    #
    #1. **Initial State**: 
    #   - `n` is an input integer.
    #   - `k` is an input integer.
    #   - `l` is equal to `(n + k - 1) // (k * 2 + 1)`.
    #   - `res` is an empty list.
    #
    #2. **Loop Code**:
    #   ```
    #   for i in range(l):
    #       res.append(i * (k * 2 + 1) + 1)
    #   ```
    #
    #3. **Output States after Executing the Loop a Few Times**:
    #   - After 1 time: `res` contains the value 1, `i` is 0.
    #   - After 2 times: `res` contains the values 1 and `2 * k + 2` (which can be calculated as `1 * (k * 2 + 1) + 1`), `i` is 1.
    #   - After 3 times: `res` contains the values 1, `2 * k + 2`, and `4 * k + 3` (which can be calculated as `2 * (k * 2 + 1) + 1`), `i` is 2.
    #
    #From the loop code, it's clear that `res` is being populated with values calculated as `i * (k * 2 + 1) + 1` for each `i` in the range from 0 to `l-1`. 
    #
    #- If `l` is 0 (meaning `(n + k - 1) // (k * 2 + 1)` equals 0), the loop will not execute, and `res` will remain an empty list. This happens when `n + k - 1 < k * 2 + 1`.
    #- If `l` is greater than 0, the loop will execute `l` times, appending `l` values to `res`. Each value appended is of the form `i * (k * 2 + 1) + 1` for `i` ranging from 0 to `l-1`.
    #
    #**Calculating the Final State**:
    #
    #- `n` and `k` retain their original values as input integers.
    #- `l` is determined by the formula `(n + k - 1) // (k * 2 + 1)`, and its value determines how many times the loop executes.
    #- `res` will contain a list of values where each value is calculated as `i * (k * 2 + 1) + 1` for `i` from 0 to `l-1`. If `l` is 0, `res` remains an empty list.
    #- `i` will be `l-1` after the loop finishes, because the loop iterates over the range from 0 to `l-1`.
    #
    #**Output State**: **`n` is an input integer, `k` is an input integer, `l` is `(n + k - 1) // (k * 2 + 1)`, `res` is a list containing values from 1 to `(l-1) * (k * 2 + 1) + 1` (or empty if `l` is 0), and `i` is `l-1` if `l` > 0, otherwise, `i` remains undefined as the loop doesn't execute.**
    print(l)
    print(' '.join(map(str, res)))
#Overall this is what the function does:The function calculates and prints the integer division result of `(n + k - 1)` by `(k * 2 + 1)`, and a list of numbers in arithmetic progression, where the first term is 1, the common difference is `(k * 2 + 1)`, and the number of terms is determined by the integer division result. The function accepts two input parameters, `n` and `k`, which are positive and non-negative integers respectively, with constraints 1 <= `n` <= 1000 and 0 <= `k` <= 1000. The function handles edge cases where `l` is 0 (i.e., `(n + k - 1)` is less than `(k * 2 + 1)`), in which case it prints 0 and an empty list. The final state of the program includes the printed integer division result and the list of numbers in arithmetic progression.

