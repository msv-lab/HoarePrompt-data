a, b = map(int, input().split())
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

res = factorial(b) // factorial(a)
print(res % 10)
