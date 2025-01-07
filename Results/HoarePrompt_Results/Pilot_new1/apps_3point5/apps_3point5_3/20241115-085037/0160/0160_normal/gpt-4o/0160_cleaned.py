(N, K) = map(int, input().split())
A = list(map(int, input().split()))
sum_A = sum(A)

def func_1(lst):
    gcd_result = lst[0]
    for num in lst[1:]:
        gcd_result = math.gcd(gcd_result, num)
    return gcd_result

def func_2(x):
    divisors = set()
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.add(i)
            divisors.add(x // i)
    return sorted(divisors, reverse=True)
gcd_A = func_1(A)
divisors = func_2(sum_A)
for d in divisors:
    if all((a % d == 0 or (sum_A - a) % d <= K for a in A)):
        print(d)
        break