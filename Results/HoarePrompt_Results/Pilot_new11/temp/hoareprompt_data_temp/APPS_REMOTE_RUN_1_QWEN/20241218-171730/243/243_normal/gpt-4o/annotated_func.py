#State of the program right berfore the function call: n is a non-negative integer representing the value of n in n!, and the function calculates the number of trailing zeroes in n!.
def func_1(n):
    """ Return the number of trailing zeroes in n! """
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        
        power_of_5 *= 5
        
    #State of the program after the loop has been executed: `n` must be at least the final value of `power_of_5`, `count` is the sum of `n // power_of_5` for each iteration of the loop, `power_of_5` is the final value after all iterations (which will be 5 times its initial value raised to the power of the number of iterations)
    return count
    #The program returns count which is the sum of n // power_of_5 for each iteration of the loop
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns the number of trailing zeroes in `n!`. It does this by repeatedly dividing `n` by increasing powers of 5 and summing up the results. Specifically, it calculates the sum of `n // power_of_5` for each iteration of the loop where `power_of_5` starts at 5 and is multiplied by 5 in each iteration. The function handles the case where `n` is 0 by returning 0 immediately since 0! has no trailing zeroes. There are no explicit edge cases mentioned in the annotations, but the function correctly handles the scenario where `n` is 0 and all other non-negative integers.

#State of the program right berfore the function call: m is an integer such that 1 <= m <= 100,000.
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
        
    #State of the program after the loop has been executed: `m` is an integer such that \(1 \leq m \leq 100,000\); `low` is 0; `high` is \(5 \times (m + 1)\); `result` is a list of integers from `left + 1` to `right - 1` where `left` and `right` are defined such that `func_1(left) == m` and `func_1(right) == m`, and `mid` is the final value of `mid` when `func_1(mid) == m`. If no such `mid` exists, `result` remains an empty list.
    return result
    #`The program returns an empty list 'result' since no such 'mid' exists where func_1(mid) == m`
#Overall this is what the function does:The function `func_2` accepts an integer `m` within the range of 1 to 100,000. It uses binary search to find the smallest number `mid` such that `func_1(mid)` equals `m`. If such a `mid` is found, it searches for the range of numbers around `mid` where `func_1(n)` equals `m` and returns a list of these numbers. If no such `mid` exists, it returns an empty list. The function also includes a check to ensure that `func_1(mid)` equals `m` before adding numbers to the result list. However, there is a missing edge case where if the function cannot find a valid `mid`, it still returns an empty list instead of indicating that no such range exists.

