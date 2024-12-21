def func_1(x, y):
    while y:
        (x, y) = (y, x % y)
    return x

def func_2(x, y):
    return x * y // func_1(x, y)

def func_3(a, b):
    if a == b:
        return 0
    diff = abs(a - b)
    min_lcm = float('inf')
    min_k = 0
    for k in range(1, int(math.sqrt(diff)) + 1):
        if diff % k == 0:
            for candidate in [k, diff // k]:
                new_a = (a + candidate - 1) // candidate * candidate
                new_b = (b + candidate - 1) // candidate * candidate
                current_lcm = func_2(new_a, new_b)
                if current_lcm < min_lcm or (current_lcm == min_lcm and candidate < min_k):
                    min_lcm = current_lcm
                    min_k = candidate
    return min_k
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    a = int(data[0])
    b = int(data[1])
    print(func_3(a, b))