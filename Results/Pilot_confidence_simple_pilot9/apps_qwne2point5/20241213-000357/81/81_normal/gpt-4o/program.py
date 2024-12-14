import math

def count_good_pairs(l, r, x, y):
    if y % x != 0:
        return 0

    z = y // x
    count = 0
    
    for i in range(1, int(math.sqrt(z)) + 1):
        if z % i == 0:
            a = i * x
            b = (z // i) * x
            if l <= a <= r and l <= b <= r and math.gcd(a, b) == x and (a * b) // math.gcd(a, b) == y:
                if a == b:
                    count += 1
                else:
                    count += 2

    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    l, r, x, y = map(int, input().strip().split())
    print(count_good_pairs(l, r, x, y))
