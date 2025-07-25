import math

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def find_min_k(a, b):
    if a == b:
        return 0

    diff = abs(a - b)
    min_lcm = float('inf')
    min_k = 0

    for k in range(1, int(math.sqrt(diff)) + 1):
        if diff % k == 0:
            # Check both k and diff // k as possible values for the smallest k
            for candidate in [k, diff // k]:
                new_a = (a + candidate - 1) // candidate * candidate
                new_b = (b + candidate - 1) // candidate * candidate
                current_lcm = lcm(new_a, new_b)
                if current_lcm < min_lcm or (current_lcm == min_lcm and candidate < min_k):
                    min_lcm = current_lcm
                    min_k = candidate

    return min_k

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    a = int(data[0])
    b = int(data[1])
    print(find_min_k(a, b))
