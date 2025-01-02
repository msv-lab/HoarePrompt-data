ans = 0
(a, b) = [int(x) for x in sys.stdin.readline().strip().split()]
while a > 0 and b > 0:
    ans *= 3
    ans += (3 - a % 3 + b % 3) % 3
    a //= 3
    b //= 3
print(ans)