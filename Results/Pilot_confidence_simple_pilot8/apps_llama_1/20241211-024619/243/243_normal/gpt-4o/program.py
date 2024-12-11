def count_trailing_zeroes(n):
    """ Return the number of trailing zeroes in n! """
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5
    return count

def find_numbers_with_trailing_zeroes(m):
    """ Find all numbers n such that n! ends with exactly m trailing zeroes """
    low, high = 0, 5 * (m + 1)
    result = []

    while low <= high:
        mid = (low + high) // 2
        zeroes = count_trailing_zeroes(mid)
        if zeroes < m:
            low = mid + 1
        elif zeroes > m:
            high = mid - 1
        else:
            result = []
            left = mid
            while count_trailing_zeroes(left) == m:
                left -= 1
            right = mid + 1
            while count_trailing_zeroes(right) == m:
                right += 1
            result = list(range(left + 1, right))
            break

    return result

# Read input
m = int(input())

# Find result
result = find_numbers_with_trailing_zeroes(m)

# Output result
if result:
    print(len(result))
    print(' '.join(map(str, result)))
else:
    print(0)
