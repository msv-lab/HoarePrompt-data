def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
primes = []
for i in range(2, n):
    if is_prime(i):
        primes.append(i)

for k in range(1, 4):
    for p1 in primes:
        if k == 1:
            if p1 == n:
                print(k)
                print(p1)
                exit()
        else:
            for p2 in primes:
                if k == 2:
                    if p1 + p2 == n:
                        print(k)
                        print(p1, p2)
                        exit()
                else:
                    for p3 in primes:
                        if p1 + p2 + p3 == n:
                            print(k)
                            print(p1, p2, p3)
                            exit()
