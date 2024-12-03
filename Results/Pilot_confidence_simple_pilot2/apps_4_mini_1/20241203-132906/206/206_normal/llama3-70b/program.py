def count_zeros(n, b):
    count = 0
    i = b
    while i <= n:
        count += n // i
        i *= b
    return count

n, b = map(int, input().split())
print(count_zeros(n, b))
