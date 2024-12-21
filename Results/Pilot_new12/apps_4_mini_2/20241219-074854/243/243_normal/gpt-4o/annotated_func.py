#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n.
def func_1(n):
    """ Return the number of trailing zeroes in n! """
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        
        power_of_5 *= 5
        
    #State of the program after the loop has been executed: `power_of_5` is the smallest power of 5 that is greater than `n`, `count` is equal to `floor(n/5) + floor(n/25) + floor(n/125) + ...` until the power of 5 exceeds `n`.
    return count
    #The program returns count, which is calculated as floor(n/5) + floor(n/25) + floor(n/125) + ... until the power of 5 exceeds n.
#Overall this is what the function does:The function accepts a positive integer `n` (where `n` is at least 1) and returns the number of trailing zeroes in the factorial of `n` (denoted as `n!`). It calculates this by counting the total number of factors of 5 present in the numbers from 1 to `n`, since each pair of factors of 2 and 5 contribute to a trailing zero, and factors of 2 are more abundant than factors of 5 in factorials. The calculation iteratively sums the integer division of `n` by increasing powers of 5 until the power of 5 exceeds `n`. The return value is the accumulated count of these factors. There is no explicit handling of cases where `n` is less than 1, but per the function's precondition, it is assumed that `n` is always a valid positive integer.

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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, `result` contains the list of integers from `left + 1` to `right - 1`, where `func_1(left)` equals `m` and `func_1(right)` does not equal `m`, and `m` is a positive integer such that 1 ≤ `m` ≤ 100000.
    return result
    #The program returns the list of integers from `left + 1` to `right - 1`, where `low` is greater than `high`, `result` contains these integers, and `m` is a positive integer such that 1 ≤ `m` ≤ 100000.
#Overall this is what the function does:The function `func_2` accepts a positive integer `m` where \( 1 \leq m \leq 100000 \) and returns a list of integers such that the factorial of each integer in that list ends with exactly `m` trailing zeroes. The function performs a binary search to determine the range of integers whose factorials yield the desired trailing zero count. If no integers meet this criteria, the function will return an empty list. The function also handles edge cases, such as when there are no integers with `m` trailing zeroes. The final state of the function is that it will return a list containing those integers in the specified range or an empty list if no such integers exist.

