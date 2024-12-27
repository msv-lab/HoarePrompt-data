import bisect
import sys
import fileinput

def getPrimes():
    primes = []
    values = [True for p in range(2, (10**6) + 10)]
    p = 2
    while p <= (10**6):
        if values[p] == True:
            primes.append(p)
            for m in range(p*2, (10**6), p):
                values[m] = False
        p += 1
    del values
    return primes

a = int(input(""))
arr = []
primes = getPrimes()
while a >= 0:
    position = bisect.bisect_left(primes, a)
    if primes[position] > a or (primes[position] == a and a not in [2, 3]) :
        position -= 1
        if a - 1 == primes[position]:
            position -= 1
    arr.append(primes[position])
    a -= primes[position]
    if a == 0:
        break

print(len(arr))
print (" ".join([str(word) for word in arr]))