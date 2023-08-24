import math

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k % 2 == 1:
    print(0)
else:
    num_zeros = a.count(0)
    num_ones = a.count(1)
    if num_zeros == 0 or num_ones == 0:
        print(1)
    else:
        p = math.factorial(num_zeros + num_ones - 2) % (10**9 + 7)
        q = (math.factorial(num_zeros - 1) * math.factorial(num_ones - 1)) % (10**9 + 7)
        q_inv = pow(q, 10**9 + 5, 10**9 + 7)
        result = (p * q_inv) % (10**9 + 7)
        print(result)