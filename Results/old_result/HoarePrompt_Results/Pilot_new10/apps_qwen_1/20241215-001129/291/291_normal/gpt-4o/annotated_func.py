#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^9.
def func_1(n):
    min_segments_needed = float('inf')
    for a in range(1, int(math.sqrt(n)) + 1):
        b = (n + a - 1) // a
        
        segments_needed = 2 * (a + b)
        
        min_segments_needed = min(min_segments_needed, segments_needed)
        
    #State of the program after the  for loop has been executed: To determine the final state of the variables after the loop completes all its iterations, let's analyze the loop step-by-step.
    #
    #### Loop Analysis
    #
    #1. **Initialization**:
    #   - `n` is an integer such that \(1 \leq n \leq 10^9\).
    #   - `min_segments_needed` is initialized to infinity.
    #
    #2. **Loop Execution**:
    #   - The loop iterates over `a` from 1 to `int(math.sqrt(n)) + 1`.
    #   - For each iteration, it calculates:
    #     - `b = (n + a - 1) // a`
    #     - `segments_needed = 2 * (a + b)`
    #   - It updates `min_segments_needed` to be the minimum of its current value and `segments_needed`.
    #
    #3. **Understanding the Loop**:
    #   - The goal is to find the minimum `segments_needed` which is defined as \(2 \times (a + b)\), where \(b\) is computed as \((n + a - 1) // a\).
    #   - The loop effectively tries different values of `a` to find the combination that minimizes `segments_needed`.
    #
    #### Iteration Observations
    #
    #- **First Iteration**:
    #  - `a = 1`
    #  - `b = (n + 1 - 1) // 1 = n`
    #  - `segments_needed = 2 * (1 + n) = 2 * (n + 1)`
    #  - `min_segments_needed` is updated to `2 * (n + 1)`.
    #
    #- **Second Iteration**:
    #  - `a = 2`
    #  - `b = (n + 2 - 1) // 2 = (n + 1) // 2`
    #  - `segments_needed = 2 * (2 + (n + 1) // 2)`
    #  - `min_segments_needed` is updated to the minimum of `2 * (n + 1)` and `2 * (2 + (n + 1) // 2)`.
    #
    #- **Third Iteration**:
    #  - `a = 3`
    #  - `b = (n + 3 - 1) // 3 = (n + 2) // 3`
    #  - `segments_needed = 2 * (3 + (n + 2) // 3)`
    #  - `min_segments_needed` is updated to the minimum of the previous value and `2 * (3 + (n + 2) // 3)`.
    #
    #### Final State After All Iterations
    #
    #- The loop will iterate until `a` reaches `int(math.sqrt(n)) + 1`.
    #- The variable `min_segments_needed` will be updated to the minimum value of `2 * (a + b)` for all valid `a`.
    #
    #Since the loop will try all possible values of `a` from 1 to `int(math.sqrt(n)) + 1`, the final value of `min_segments_needed` will be the smallest value obtained from these calculations.
    #
    #### Output State
    #
    #After the loop has completed all its iterations, the values of the variables will be as follows:
    #
    #- `min_segments_needed` will be the minimum value of `2 * (a + (n + a - 1) // a)` for all `a` from 1 to `int(math.sqrt(n)) + 1`.
    #- `a` and `b` will no longer be relevant since the loop has finished.
    #- `n` remains unchanged.
    #
    #Thus, the output state is:
    #
    #**Output State: `min_segments_needed` is the minimum value of \(2 \times (a + \frac{n + a - 1}{a})\) for all \(a\) from 1 to \(\text{int}(\sqrt{n}) + 1\), `n` is an integer such that \(1 \leq n \leq 10^9\).**
    return min_segments_needed
    #`min_segments_needed` is the minimum value of \(2 \times (a + \frac{n + a - 1}{a})\) for all \(a\) from 1 to \(\text{int}(\sqrt{n}) + 1\), where `n` is an integer such that \(1 \leq n \leq 10^9\).
#Overall this is what the function does:The function accepts an integer `n` such that \(1 \leq n \leq 10^9\), and returns the minimum value of \(2 \times (a + \frac{n + a - 1}{a})\) for all \(a\) from 1 to \(\text{int}(\sqrt{n}) + 1\). The function iterates through all possible values of `a` within the specified range and calculates the corresponding `segments_needed` for each value of `a`, updating the `min_segments_needed` to the smallest value found.

