def divisors(n):
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            factors[i] = factors.get(i, 0) + 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = factors.get(nn, 0) + 1
 
    primes = list(factors.keys())
 
    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime
 
    # in python3, `yield from generate(0)` would also work
    for factor in generate(0):
        yield factor
 
for _  in range(int(input())):
    # n = int(input())
    n, x = map(int, input().split())
    # arr = list(map(int, input().split()))
 
    ans = 1
 
    h = n-x
    ans = set(k for k in divisors(h) if not k%2 and k/2+1 >= x) # divisors of h >=  max(x, 2)
 
    # print(list(divisors(h)))
 
    ans2 = set()
    if x!=1:
        h = n + x-2
        ans2 = set(k for k in divisors(h) if not k%2 and k/2+1 >= x)
 
    # for f in sorted(ans):
    #     print(f//2+1, end='\t')
    # print()
 
    # print(sorted(ans))
    # print(sorted(ans2))
    ans = ans.union(ans2)
    print(len(ans))
    # print()