n = int(input())

def func_1(n):
    if n < 6:
        return 0
    count = 0
    for a in range(1, n // 4 + 1):
        b = a
        rem = n - 2 * (a + b)
        if rem > 0 and rem % 2 == 0:
            if a != rem // 2:
                count += 1
    return count
print(func_1(n))