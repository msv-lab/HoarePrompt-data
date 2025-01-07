#State of the program right berfore the function call: n is a positive integer such that n >= 0.
def func_1(n):
    """ Return the number of trailing zeroes in n! """
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        
        power_of_5 *= 5
        
    #State of the program after the loop has been executed: `n` is less than 5^k (where k is the number of iterations executed), `count` is the total count of all integers divisions from n by 5, 25, 125, ..., until `n` is less than the next power of 5. The final value of `power_of_5` after the loop will be `5^{number of iterations executed + 1}`.
    return count
    #The program returns the total count of all integers divisions from n by 5, 25, 125, ..., until n is less than the next power of 5.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns the count of trailing zeroes in the factorial of `n`. It does this by counting how many times `n` can be divided by powers of 5 until `n` is less than the next power of 5.

#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 100,000.
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
        
    #State of the program after the loop has been executed: `low` is greater than `high`, if `zeroes` is less than `m`, then `low` is greater than 5 * (`m` + 1); if `zeroes` is greater than `m`, then `high` is less than 5 * (`m` + 1). If `zeroes` equals `m`, then `result` contains a list of integers from `left + 1` to `right - 1`, where `left` is the last index where `func_1(left) == m` and `right` is the first index where `func_1(right) != m`.`
    return result
    #The program returns a list of integers from `left + 1` to `right - 1`, where `left` is the last index satisfying `func_1(left) == m` and `right` is the first index satisfying `func_1(right) != m`.
#Overall this is what the function does:The function accepts a positive integer `m` and returns a list of integers `n` such that `n!` (n factorial) ends with exactly `m` trailing zeroes. The range of `n` is determined by performing a binary search based on the output of the function `func_1`, which counts the trailing zeroes in `n!`. If no such integers exist, an empty list is returned.

