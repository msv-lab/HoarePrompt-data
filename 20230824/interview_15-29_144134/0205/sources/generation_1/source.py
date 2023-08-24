def count_trailing_zeros(n, b):
    count = 0
    while n > 0:
        n //= b
        count += n
    return count

n, b = map(int, input().split())
print(count_trailing_zeros(n, b))