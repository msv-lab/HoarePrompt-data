n = input()
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def solve(s):
    i = gcd(180, s)
    k = s / i
    n = 180 /i
    # print(n, k)
    if (n <= (k + 2)):
        n = n * 2
    print(n)
for _ in range(n):
    s = input()
    solve(s)
