import sys
import math

if sys.subversion[0] == "PyPy":
    import io, atexit

    sys.stdout = io.BytesIO()
    atexit.register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))

    sys.stdin = io.BytesIO(sys.stdin.read())
    input = lambda: sys.stdin.readline().rstrip()
RS = raw_input
RA = lambda x=int: map(x, RS().split())
RN = lambda x=int: x(RS())


def solve():
    check_pairwise()
    check_set()
    return


def check_pairwise():
    active = set()
    for i in range(0, n):
        pp = getprimes(a[i])
        for p in pp:
            if p in active:
                return
            else:
                active.add(p)
    print("pairwise coprime")
    exit()



def check_set():
    active = getprimes(a[0])
    for i in range(1, n):
        if not a[i] % a[i-1] == 0:
            rm = []
            for act in active:
                if not a[i] % act == 0:
                    rm.append(act)
            for r in rm:
                active.remove(r)
                if not active:
                    print("setwise coprime")
                    exit()
    if not active:
        print("setwise coprime")
        exit()
    print("not coprime")
    exit()




def getprimes(num):
    if num in primes:
        return set([num])
    pp = set()
    for p in iterprimes:
        if p > int(math.sqrt(num)+2):
            break
        if num % p == 0:
            pp.add(p)

    return pp




def n_primes(n):
    nums = list(range(0, n + 1))
    primes = []
    for i in range(2, n + 1):
        num = nums[i]
        if num != 0:
            primes.append(num)
            for i in range(0, n // num + 1):
                nums[i * num] = 0
    return primes


n = RN()
a = sorted(RA())
iterprimes = n_primes(10 ** 6)
primes = set(iterprimes)
solve()
