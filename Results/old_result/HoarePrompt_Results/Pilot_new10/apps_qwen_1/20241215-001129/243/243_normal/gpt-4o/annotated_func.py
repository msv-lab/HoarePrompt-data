#State of the program right berfore the function call: n is a non-negative integer representing the value of n in n!, and the function calculates the number of trailing zeroes in n!.
def func_1(n):
    """ Return the number of trailing zeroes in n! """
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        
        power_of_5 *= 5
        
    #State of the program after the loop has been executed: `n` is a non-negative integer, `count` is the sum of `n // 5`, `n // 25`, `n // 125`, ..., `power_of_5` is the final value which is `5^k` where `k` is the number of times the loop executed, and `n` must have been at least `5^k`.
    return count
    #The program returns count, which is the sum of n // 5, n // 25, n // 125, ..., where each term is n divided by increasing powers of 5 until n is less than the next power of 5
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns the count of trailing zeroes in \( n! \) by calculating the sum of \( n // 5 \), \( n // 25 \), \( n // 125 \), ..., where each term is \( n \) divided by increasing powers of 5 until \( n \) is less than the next power of 5. This calculation accurately determines the number of trailing zeroes in the factorial of `n`.

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
        
    #State of the program after the loop has been executed: `m` is an integer such that \(1 \leq m \leq 100,000\). `low` and `high` are updated until `low` exceeds `high`. `result` is a list of integers from `left + 1` to `right - 1` where `left` and `right` are determined based on the conditions within the loop. If `zeroes < m`, then `low` is updated to `mid + 1` or `mid - 1` and `high` remains `5 \times (m + 1)`. If `zeroes > m`, then `low` remains unchanged and `high` is updated to `mid - 1`. If `zeroes == m`, then `left` is found by decrementing from `mid` until `func_1(left) != m` and `right` is found by incrementing from `mid + 1` until `func_1(right) != m`. Finally, `result` is set to the range of integers from `left + 1` to `right - 1`.
    return result
    #`The program returns a list of integers from left + 1 to right - 1, where left and right are determined based on the conditions within the loop: if zeroes < m, then low is updated to mid + 1 or mid - 1, and high remains 5 * (m + 1); if zeroes > m, then low remains unchanged and high is updated to mid - 1; if zeroes == m, then left is found by decrementing from mid until func_1(left) != m, and right is found by incrementing from mid + 1 until func_1(right) != m.`
#Overall this is what the function does:The function `func_2` accepts an integer `m` such that \(1 \leq m \leq 100,000\) and returns a list of integers `n` for which `n!` (n factorial) ends with exactly `m` trailing zeroes. The function uses binary search to find the range of such integers, updating the bounds `low` and `high` based on the count of trailing zeroes returned by `func_1(mid)`. If the count matches `m`, it further narrows down the exact range by finding the boundaries where the count of trailing zeroes changes.

