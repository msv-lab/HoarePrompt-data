#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2·10^9.
def func_1(n):
    ways = 0
    for a in range(1, n // 2 + 1):
        for b in range(a, (n - a) // 2 + 1):
            if a != b and 2 * (a + b) == n:
                ways += 1
        
    #State of the program after the  for loop has been executed: Let's analyze the given Python loop and its behavior step by step.
    #
    #### Step 1: Analyze the Code and Initial State
    #The loop iterates over possible values of `a` and `b` within specified ranges, checking if the condition \(2 \times (a + b) == n\) holds and \(a \neq b\). The variable `ways` is incremented each time this condition is met.
    #
    #### Step 2: Track Variable Changes
    #- **`n`**: The value of `n` remains constant throughout the loop as it is not modified inside the loop.
    #- **`ways`**: This variable starts at 0 and is incremented each time the condition \(2 \times (a + b) == n\) and \(a \neq b\) is satisfied.
    #- **`a` and `b`**: These variables take on values within their respective ranges during each iteration but are not stored outside the loop for future use.
    #
    #### Step 3: Summarize the Loop Behavior
    #The loop checks every possible pair \((a, b)\) where \(a\) ranges from 1 to \(\frac{n}{2}\) and \(b\) ranges from \(a\) to \(\frac{n - a}{2}\). It increments `ways` if \(2 \times (a + b) == n\) and \(a \neq b\).
    #
    #### Step 4: Verify Relationships
    #- The loop will execute if \(n\) is even, because for odd \(n\), there can't be a pair \((a, b)\) such that \(2 \times (a + b) == n\).
    #- For even \(n\), the loop will iterate through all valid pairs \((a, b)\) until it finds all pairs that satisfy the condition.
    #
    #### Final Output State Calculation
    #To find the final value of `ways`, we need to determine all pairs \((a, b)\) such that \(2 \times (a + b) == n\) and \(a \neq b\).
    #
    #Since \(2 \times (a + b) == n\), it simplifies to \(a + b == \frac{n}{2}\). We need to count all pairs \((a, b)\) where \(1 \leq a < b \leq \frac{n}{2}\) and \(a + b == \frac{n}{2}\).
    #
    #For each valid \(a\), there is exactly one corresponding \(b\) such that \(b = \frac{n}{2} - a\) and \(a \neq b\). Therefore, the number of valid pairs is half the number of integers from 1 to \(\frac{n}{2}\), minus one (to exclude the case where \(a = b\)).
    #
    #Thus, the number of valid pairs is \(\left\lfloor \frac{\frac{n}{2}}{2} \right\rfloor = \left\lfloor \frac{n}{4} \right\rfloor\).
    #
    #### Final Output State
    #Output State: `ways` is equal to \(\left\lfloor \frac{n}{4} \right\rfloor\).
    return ways
    #`ways` is equal to \(\left\lfloor \frac{n}{4} \right\rfloor\)
#Overall this is what the function does:The function `func_1` accepts a single parameter `n`, which must be a positive integer between 1 and \(2 \times 10^9\). The function calculates the number of unique pairs \((a, b)\) such that \(a + b = \frac{n}{2}\) and \(a \neq b\). The final state of the program after the function concludes is that it returns the value \(\left\lfloor \frac{n}{4} \right\rfloor\).

