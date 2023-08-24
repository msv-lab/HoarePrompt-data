
n = int(input())
s = int(input())

def base_sum(b, n):
    if n < b:
        return n
    return base_sum(b, n // b) + (n % b)

if n == s:
    print(n + 1)
else:
    for b in range(2, int(n ** 0.5) + 2):
        if base_sum(b, n) == s:
            print(b)
            break
    else:
        for p in range(int(n ** 0.5), 0, -1):
            b = (n - s) // p + 1
            if base_sum(b, n) == s:
                print(b)
                break
        else:
            print(-1)
