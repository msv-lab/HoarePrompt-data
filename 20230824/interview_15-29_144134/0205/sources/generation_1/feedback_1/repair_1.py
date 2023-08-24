def count_trailing_zeros(n, b):
    if n == 0:
        return 0

    count = 0
    while n > 0:
        n /= b
        count += n
    return int(count)

n, b = map(int, input().split())
print(count_trailing_zeros(n, b))