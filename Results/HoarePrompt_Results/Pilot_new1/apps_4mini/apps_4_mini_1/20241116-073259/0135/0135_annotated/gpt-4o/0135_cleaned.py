(n, k) = map(int, input().split())

def func_1(n, k):
    if k >= n:
        return 'No'
    seen_remainders = set()
    for i in range(1, k + 1):
        remainder = n % i
        if remainder in seen_remainders:
            return 'No'
        seen_remainders.add(remainder)
    return 'Yes'
print(func_1(n, k))