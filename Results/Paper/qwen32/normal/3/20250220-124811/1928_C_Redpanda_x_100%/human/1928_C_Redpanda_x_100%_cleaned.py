def func_1(n):
    factors = {}
    nn = n
    i = 2
    while i * i <= nn:
        while nn % i == 0:
            factors[i] = factors.get(i, 0) + 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = factors.get(nn, 0) + 1
    primes = list(factors.keys())

    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k + 1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                for _ in range(factors[prime] + 1):
                    yield (factor * prime_to_i)
                    prime_to_i *= prime
    for factor in generate(0):
        yield factor
for _ in range(int(input())):
    (n, x) = map(int, input().split())
    ans = 1
    h = n - x
    ans = set((k for k in func_1(h) if not k % 2 and k / 2 + 1 >= x))
    ans2 = set()
    if x != 1:
        h = n + x - 2
        ans2 = set((k for k in func_1(h) if not k % 2 and k / 2 + 1 >= x))
    ans = ans.union(ans2)
    print(len(ans))