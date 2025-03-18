n = int(input())

# Number of ways to split the stick into four parts such that it's possible to form a rectangle but not a square
def count_ways(n):
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

print(count_ways(n))
