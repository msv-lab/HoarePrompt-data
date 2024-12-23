#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    """ Return the number of trailing zeroes in n! """
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        
        power_of_5 *= 5
        
    #State of the program after the loop has been executed: `power_of_5` is the smallest power of 5 greater than `n`, `count` equals the original value of `trailing_zeroes` which is the sum of `n` divided by all powers of 5 until the quotient is less than 1, and this sum also represents the number of trailing zeroes in the factorial of the original value of `n`.
    return count
    #The program returns the number of trailing zeroes in the factorial of the original value of `n`, which is equal to the sum of `n` divided by all powers of 5 until the quotient is less than 1
#Overall this is what the function does:The function accepts a single parameter `n`, a positive integer, and returns the number of trailing zeroes in the factorial of `n`, calculated as the sum of `n` divided by all powers of 5 until the quotient is less than 1. The function handles all positive integer inputs, and the returned value represents the count of factors of 5 in all the numbers from 1 to `n`, which in turn determines the number of trailing zeroes in the factorial of `n`. The function does not perform any error checking on the input, so it assumes that `n` will always be a positive integer. If `n` were to be 0 or a negative integer, the function would still return a value, but this would not accurately reflect the number of trailing zeroes in the factorial of `n`, as the factorial is only defined for non-negative integers and the function does not handle these edge cases. For any positive integer `n`, the function will return the correct count of trailing zeroes in `n!`.

#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 100 000
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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, or `low` and `high` are unchanged if `func_1(mid)` equals `m` and the loop breaks, `m` is unchanged, and `result` is either an empty list if no `mid` satisfies `func_1(mid) == m`, or a list of integers from `left + 1` to `right - 1` where `left` and `right` are the boundaries for which `func_1(x)` equals `m`, with `left` being the first value less than `mid` for which `func_1(left)` does not equal `m`, and `right` being the first value greater than `mid` for which `func_1(right)` does not equal `m`.
    return result
    #The program returns 'result' which is either an empty list if no 'mid' satisfies 'func_1(mid) == m', or a list of integers from 'left + 1' to 'right - 1' where 'left' and 'right' are the boundaries for which 'func_1(x)' equals 'm', with 'left' being the first value less than 'mid' for which 'func_1(left)' does not equal 'm', and 'right' being the first value greater than 'mid' for which 'func_1(right)' does not equal 'm'
#Overall this is what the function does:The function func_2 accepts a single parameter, a positive integer m between 1 and 100,000, and returns a list of integers. The returned list represents the range of values for which the function func_1 returns exactly m trailing zeroes when calculating the factorial of a number. If no such range exists, the function returns an empty list. The function iteratively searches for the range of values that satisfy this condition using a binary search approach and then expands around the found value to determine the exact range. After execution, the function's state is reset, with the only lasting result being the returned list of integers or an empty list if no matching range is found. The function does not modify the input parameter m and does not have any side effects. The returned list includes all integers from the first value greater than the lower boundary (for which func_1 does not return m) plus one, to the last value less than the upper boundary (for which func_1 does not return m) minus one. The function handles edge cases where no such range exists by returning an empty list.

