n, m = map(int, input().split())

count = 0

while n != m:
    if n > m:
        n -= 1
        count += 1
    elif m % 2 == 0:
        m //= 2
        count += 1
    else:
        m += 1
        count += 1

print(count)