(n, k) = map(int, input().split())
divisors = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        divisors.append(i)
        if i * i != n:
            divisors.append(n // i)
divisors.sort()
if k > len(divisors):
    print(-1)
else:
    print(divisors[k - 1])