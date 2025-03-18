#State of the program right berfore the function call: n is a positive integer such that n ≥ 0.
def func_1(n):
    """ Return the number of trailing zeroes in n! """
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        
        power_of_5 *= 5
        
    #State of the program after the loop has been executed: `power_of_5` is the smallest power of 5 greater than the original value of `n`, `count` is the sum of all integer divisions of `n` by each power of 5 up to the last one that is less than or equal to `n`, and `n` remains as the original value.
    return count
    #The program returns the sum of all integer divisions of n by each power of 5 up to the smallest power of 5 greater than the original value of n.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns the number of trailing zeroes in the factorial of `n`, calculated by summing the integer divisions of `n` by increasing powers of 5 until the power exceeds `n`.

#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 100000.
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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, `result` contains the integers between the last valid `left + 1` and `right - 1`, based on the initial value of `m`, where `zeroes` equals `m`. If the loop did not execute, then `result` remains an empty list and `low` is still 0 while `high` is 5 * (initial `m` + 1).
    return result
    #The program returns an empty list 'result' since the loop did not execute, and 'low' remains 0 while 'high' equals 5 * (initial m + 1).
#Overall this is what the function does:The function accepts a positive integer `m` and finds all integers `n` such that `n!` has exactly `m` trailing zeroes. It uses a binary search to determine the range of `n` values that produce `m` trailing zeroes. If no such integers exist, it returns an empty list.

