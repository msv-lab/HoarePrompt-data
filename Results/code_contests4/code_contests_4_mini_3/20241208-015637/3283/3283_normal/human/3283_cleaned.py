n = abs(input())
d = int(ceil((sqrt(1 + 8 * n) - 1) / 2))
print[[0, 2, 1, 0], [1, 0, 0, 2]][n % 2][d % 4] + d