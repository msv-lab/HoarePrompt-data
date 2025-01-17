def sum_of_digits(x):
    return sum(int(digit) for digit in str(x))

def count_really_big_numbers(n, s):
    left, right = s, n
    while left <= right:
        mid = (left + right) // 2
        if mid - sum_of_digits(mid) >= s:
            right = mid - 1
        else:
            left = mid + 1
    if left > n:
        return 0
    return n - left + 1

n, s = map(int, input().split())
print(count_really_big_numbers(n, s))
