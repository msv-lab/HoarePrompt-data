#State of the program right berfore the function call: n and m are non-negative integers such that 0 <= n, m <= 1,000,000 and n + m > 0.
def func():
    n, m = map(int, input().split())

towers = set()
    for i in range(1, n + 1):
        towers.add(i * 2)
        
    #State of the program after the  for loop has been executed: Output State: `i` is `n`, `n` must be greater than or equal to 1, `towers` is a set containing `{2, 4, 6, ..., 2*n}`.
    #
    #### Explanation:
    #
    #1. **Analyze the Code and Initial State**:
    #   - The loop iterates over the range from 1 to `n + 1`.
    #   - In each iteration, the value `i * 2` is added to the set `towers`.
    #
    #2. **Track Variable Changes**:
    #   - `i` is incremented by 1 in each iteration of the loop.
    #   - `n` remains unchanged as it is defined in the loop's initialization.
    #   - `towers` is updated in each iteration by adding `i * 2`.
    #
    #3. **Summarize the Loop Behavior**:
    #   - After the loop completes, `i` will be `n + 1` because the loop runs from 1 to `n + 1` but `i` starts from 1.
    #   - The variable `n` must be greater than or equal to 1 for the loop to run at least once.
    #   - The set `towers` contains the elements `2, 4, 6, ..., 2*n`, which are the even numbers up to `2*n`.
    #
    #4. **Verify Relationships**:
    #   - The loop adds `i * 2` to `towers` in each iteration, so after `n` iterations, `towers` contains `{2, 4, 6, ..., 2*n}`.
    #   - The final value of `i` is `n + 1`, but since the loop condition checks `range(1, n + 1)`, the last value of `i` that gets checked is `n`.
    #
    #Thus, the final state after the loop has completed all its iterations is:
    #Output State: `i` is `n`, `n` must be greater than or equal to 1, `towers` is a set containing `{2, 4, 6, ..., 2*n}`.
    for i in range(1, m + 1):
        towers.add(i * 3)
        
    #State of the program after the  for loop has been executed: Output State: `i` is `m + 1`; `m` must be greater than or equal to 1; `towers` is a set containing `{3, 6, 9, ..., 3*m}`.
    print(max(towers))
#Overall this is what the function does:The function accepts no parameters and reads two non-negative integers \(n\) and \(m\) from the input. It then creates a set `towers` containing the first \(n\) even numbers starting from 2 and the first \(m\) multiples of 3 starting from 3. Finally, it prints the maximum value present in the `towers` set. If either \(n\) or \(m\) is 0, the set `towers` will only contain the appropriate sequence of numbers based on the non-zero input.

