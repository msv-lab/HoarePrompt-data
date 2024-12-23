n = int(input())
for a in range(n // 1234567 + 1):
    for b in range((n - a * 1234567) // 123456 + 1):
        c = (n - a * 1234567 - b * 123456) // 1234
        if a * 1234567 + b * 123456 + c * 1234 == n:
            print('YES')
            exit()
print('NO')