#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    """ Return the number of trailing zeroes in n! """
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        
        power_of_5 *= 5
        
    #State of the program after the loop has been executed: To determine the output state after all iterations of the loop have executed, let's analyze the pattern from the given output states after the loop executes 1, 2, and 3 times.
    #
    #1. **First Execution**: 
    #   - `n` must be greater than or equal to 5.
    #   - `count` becomes `count + n // 5`.
    #   - `power_of_5` becomes 25.
    #
    #2. **Second Execution**: 
    #   - `n` must be greater than or equal to 25 (which is 5^2).
    #   - `count` becomes `count + n // 5 + n // 25`.
    #   - `power_of_5` becomes 125 (which is 5^3).
    #
    #3. **Third Execution**: 
    #   - `n` must be greater than or equal to 125 (which is 5^3).
    #   - `count` is updated by adding `n // 125` to its previous value.
    #   - `power_of_5` becomes 625 (which is 5^4).
    #
    #**Pattern Observation**:
    #- The loop continues as long as `n` is greater than or equal to the current `power_of_5`.
    #- `count` accumulates the integer division of `n` by powers of 5, starting from 5^1, 5^2, 5^3, and so on, as long as `n` is greater than or equal to the respective power of 5.
    #- `power_of_5` is multiplied by 5 at each iteration, effectively increasing its power by 1.
    #
    #**Final Output State**:
    #- The loop will terminate when `n` is less than the current `power_of_5`. This means `power_of_5` will be the first power of 5 that exceeds `n`.
    #- `count` will accumulate the sum of the integer divisions of `n` by all powers of 5 up to but not including the power of 5 that first exceeds `n`. This is essentially calculating the number of factors of 5 in all numbers up to `n`, considering the powers of 5.
    #- Since `n` is a non-negative integer and `count` starts at 0, once the loop terminates, `count` will hold the total count of factors of 5 in all numbers from 1 to `n`, considering all powers of 5.
    #
    #**Output State**: **`power_of_5` is the smallest power of 5 greater than `n`, `count` is the sum of `n // 5^k` for all `k` where `5^k` is less than or equal to `n`, and `n` remains unchanged as the loop does not modify `n`.**
    return count
    #The program returns the total count of factors of 5 in all numbers from 1 to `n`, which is the sum of `n // 5^k` for all `k` where `5^k` is less than or equal to `n`.
#Overall this is what the function does:The function calculates and returns the total count of factors of 5 in all numbers from 1 to `n`, where `n` is a non-negative integer. It does this by summing the integer divisions of `n` by all powers of 5 up to but not including the power of 5 that first exceeds `n`. This effectively counts the number of trailing zeroes in `n!` (n factorial). The function does not modify the input `n` and handles edge cases such as when `n` is 0 (in which case it returns 0) or when `n` is less than 5 (in which case it also returns 0), as well as any other non-negative integers. The function's output is a non-negative integer representing the total count of factors of 5 in the range from 1 to `n`.

#State of the program right berfore the function call: m is a positive integer such that 1 <= m <= 100000.
def func_2(m):
    """ Find all numbers n such that n! ends with exactly m trailing zeroes """
    low, high = 0, 5 * (m + 1)
    result = []
    while low <= high:
        mid = (low + high) // 2
        
        zeroes = func_1(mid)
        
        if zeroes < m:
            low = mid + 1
        elif zeroes > m:
            high = mid - 1
        else:
            result = []
            left = mid
            while func_1(left) == m:
                left -= 1
            right = mid + 1
            while func_1(right) == m:
                right += 1
            result = list(range(left + 1, right))
            break
        
    #State of the program after the loop has been executed: `low` is greater than `high`, and if a solution exists where `n//5 + n//25 + n//125 +... == m`, then `result` contains all such numbers `n` within the determined range; otherwise, `result` remains an empty list. The original value of `m` remains unchanged, and `high` will be less than or equal to the original `high` which is `5 * (m + 1)`.
    return result
    #The program returns a list of numbers `result` that contains all numbers `n` within the determined range where `n//5 + n//25 + n//125 +... == m`, or an empty list if no such solution exists, with `m` being the original value and the determined range being between `low` and `high` where `low` is greater than `high` and `high` is less than or equal to `5 * (m + 1)`
#Overall this is what the function does:The function `func_2` accepts a single parameter `m`, a positive integer between 1 and 100000, and returns a list of numbers `n` where the sum of the integer divisions of `n` by powers of 5 equals `m`. The returned list includes all numbers within a determined range where this condition is met, or an empty list if no such numbers exist. The function does not modify the input `m`. If a solution exists where `n//5 + n//25 + n//125 +... == m`, the function will find all consecutive numbers `n` that satisfy this condition within the determined range. The function handles edge cases where no numbers satisfy the condition, returning an empty list in such scenarios, and it is designed to efficiently search for the target numbers within a constrained range, ultimately returning a list of numbers that match the specified condition or an empty list if none are found. The upper limit of the search range is bounded by `5 * (m + 1)`, ensuring that the function remains efficient for large values of `m`.

