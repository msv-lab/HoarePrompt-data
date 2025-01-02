#State of the program right berfore the function call: l and r are non-negative integers such that 1 ≤ l ≤ r ≤ 10^18.
def func_1():
    lower, upper = map(int, raw_input().split())
    res = 0
    for val in range(1, 10):
        if lower <= val <= upper:
            res += 1
        
    #State of the program after the  for loop has been executed: Let's analyze the loop step by step to determine the final state of the variables after the loop completes all its iterations.
    #
    #### Initial State Recap:
    #- `l` and `r` are non-negative integers such that \(1 \leq l \leq r \leq 10^{18}\).
    #- `lower` is the first integer input.
    #- `upper` is the second integer input.
    #- `res` is initialized to 0.
    #
    #### Loop Analysis:
    #The loop iterates over the range from 1 to 10 (inclusive). For each `val` in this range, the loop checks if `lower <= val <= upper`. If this condition is true, `res` is incremented by 1.
    #
    #### Key Observations:
    #- The loop will always iterate exactly 9 times (from `val = 1` to `val = 9`), because the range starts at 1 and ends at 10, exclusive.
    #- Whether the condition `lower <= val <= upper` holds true or not for each iteration does not affect the number of iterations; it only affects whether `res` is incremented.
    #
    #### Final State Calculation:
    #- Regardless of the values of `lower` and `upper`, the loop will iterate 9 times, and `res` will be incremented by 1 for each iteration where the condition is met.
    #- If the condition `lower <= val <= upper` is true for any `val` in the range from 1 to 9, `res` will be incremented by 1 for those values.
    #- Therefore, the maximum value `res` can achieve is 9, but it depends on the values of `lower` and `upper`.
    #
    #### Output State:
    #Given that the loop always runs 9 times and increments `res` based on the condition `lower <= val <= upper`, we can summarize the final state as follows:
    #
    #- If the condition `lower <= val <= upper` is true for any `val` in the range from 1 to 9, `res` will be incremented by 1 for those values.
    #- The exact value of `res` will be the count of numbers between `lower` and `upper` (inclusive) that lie within the range from 1 to 9.
    #
    #Thus, the final output state is:
    #**Output State: `res` is the count of integers from 1 to 9 that satisfy `lower <= val <= upper`, `val` is the last value checked in the loop, and `l` and `r` retain their initial values.**
    for length in range(2, 19):
        for startend in range(1, 10):
            alreadyval = startend * pow(10, length - 1) + (0 if length == 1 else
                startend)
            smallestpos = max(0, (lower - alreadyval + 9) / 10)
            largestpos = min(pow(10, length - 2) - 1, (upper - alreadyval) / 10)
            res += max(0, largestpos - smallestpos + 1)
        
    #State of the program after the  for loop has been executed: 
    print(res)
#Overall this is what the function does:The function processes two inputs, `lower` and `upper`, which are the lower and upper bounds of a range of integers. It counts the number of integers within the range from 1 to 9 that fall within the specified bounds (`lower` to `upper`). Specifically, it iterates over all possible lengths of numbers from 2 to 18 digits, and for each length, it calculates the count of valid starting positions (from 1 to 9) that fall within the given range. The function then sums up these counts and prints the total count of valid integers.

