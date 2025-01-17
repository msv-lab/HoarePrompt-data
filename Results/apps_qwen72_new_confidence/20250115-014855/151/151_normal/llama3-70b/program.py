def min_tax(n):
    def max_divisor(x):
        for i in range(x-1, 0, -1):
            if x % i == 0:
                return i
    if n == 2:
        return 1
    ans = float('inf')
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            x = max_divisor(i) + max_divisor(n//i)
            ans = min(ans, x)
    return ans

n = int(input())
print(min_tax(n))
