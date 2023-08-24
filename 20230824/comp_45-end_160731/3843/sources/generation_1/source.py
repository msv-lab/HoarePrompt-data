n, m = map(int, input().split())

def count_distinct_digits(num):
    digits = set()
    while num > 0:
        digit = num % 10
        num //= 10
        digits.add(digit)
    return len(digits)

def count_distinct_times(n, m):
    count = 0
    for hour in range(n):
        for minute in range(m):
            if count_distinct_digits(hour) == len(str(hour)) and count_distinct_digits(minute) == len(str(minute)):
                count += 1
    return count

result = count_distinct_times(n, m)
print(result)