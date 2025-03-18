import math
 
def fun():
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n / ((x + y) * x), m // ((x + y) * y))
            y += 1
        x += 1
    print(cnt)
 
def main():
    t = int(input())
    for _ in range(t):
        fun()
if __name__ == "__main__":
    main()