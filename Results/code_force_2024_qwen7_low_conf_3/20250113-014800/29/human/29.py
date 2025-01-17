def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def count_pairs(n, m):
    count = 0
    for a in range(1, n + 1):
        for b in range(1, m + 1):
            if (a + b) % (b * gcd(a, b)) == 0:
                count += 1
    return count