def count_really_big_numbers(n, s):
    count = 0
    for x in range(1, n + 1):
        digit_sum = sum(int(digit) for digit in str(x))
        if x - digit_sum >= s:
            count += 1
    return count

n, s = map(int, input().split())
print(count_really_big_numbers(n, s))
