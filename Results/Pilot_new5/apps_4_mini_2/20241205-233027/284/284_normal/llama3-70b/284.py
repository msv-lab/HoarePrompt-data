def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
for m in range(1, 1001):
    if not is_prime(n * m + 1):
        print(m)
        break
