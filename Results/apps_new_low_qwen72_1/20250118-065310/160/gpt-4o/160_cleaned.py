def func_1(a, b):
    return math.gcd(a, b) == 1
n = int(input())
a = list(map(int, input().split()))
result = [a[0]]
count = 0
for i in range(1, n):
    if not func_1(result[-1], a[i]):
        result.append(1)
        count += 1
    result.append(a[i])
print(count)
print(' '.join(map(str, result)))