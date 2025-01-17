k, a, b = map(int, input().split())

if a % k == 0:
    first_divisible = a
else:
    first_divisible = a + (k - a % k)

if b % k == 0:
    last_divisible = b
else:
    last_divisible = b - (b % k)

if first_divisible > b or last_divisible < a:
    print(0)
else:
    print((last_divisible - first_divisible) // k + 1)
