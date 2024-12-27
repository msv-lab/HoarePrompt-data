import random
import time
import sys

def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)

n = int(input())
t = []

random.seed(time.time())

for iter in range(50):
    x = random.randint(2, n - 1)
    print("sqrt %s" % ((x * x) % n)) 
    sys.stdout.flush()

    s = int(input())
    if s == x or s + x == n:
        continue

    t.append(find_gcd(x + s, n))

t = sorted(t)
p = []
for i in range(len(t)):
    if t[i] != 1 and t[i] not in p:
        p.append(t[i])
        for j in range(len(t)):
            if i != j and t[j] % t[i] == 0:
                t[j] /= t[i]

p = sorted(p)
res = []
prod = 1
for x in p:
    res.append(x)
    prod *= x
    if prod == n:
        break
        
print("! %s %s" % (len(res), " ".join([str(x) for x in res])))
sys.stdout.flush()
