def func_1(n):
    """ Return the number of trailing zeroes in n! """
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5
    return count

def func_2(m):
    """ Find all numbers n such that n! ends with exactly m trailing zeroes """
    (low, high) = (0, 5 * (m + 1))
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
    return result
m = int(input())
result = func_2(m)
if result:
    print(len(result))
    print(' '.join(map(str, result)))
else:
    print(0)