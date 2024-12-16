#State of the program right berfore the function call: n is a non-negative integer, representing the number for which the factorial is calculated to determine the number of trailing zeroes.
def func_1(n):
    """ Return the number of trailing zeroes in n! """
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        
        power_of_5 *= 5
        
    #State of the program after the loop has been executed: `n` remains the same as the original value of `n`, `power_of_5` is the smallest power of 5 greater than `n`, `count` is the sum of the integer divisions of the original value of `n` by all powers of 5 that are less than or equal to the original value of `n`.
    return count
    #The program returns the sum of the integer divisions of the original value of `n` by all powers of 5 that are less than or equal to the original value of `n`.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns the number of trailing zeroes in the factorial of `n`, calculated by summing the integer divisions of `n` by all powers of 5 less than or equal to `n`.

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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, `result` is either an empty list or a list of integers from `left + 1` to `right - 1`, where `left` and `right` are determined based on the relationship between the number of trailing zeroes in the factorial of `mid` and the original value of `m`.
    return result
    #The program returns a list of integers that is either empty or contains integers from `left + 1` to `right - 1`, where the range is determined based on the relationship between the number of trailing zeroes in the factorial of `mid` and the original value of `m`.
#Overall this is what the function does:The function accepts a positive integer `m` and returns a list of consecutive integers `n` where `n!` has exactly `m` trailing zeroes, or an empty list if no such integers are found, assuming the helper function `func_1` works correctly and the input `m` is within the expected range.

