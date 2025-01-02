ifs = sys.stdin
ofs = sys.stdout

def func_1(N):
    primes = [True] * (N + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(sqrt(N)) + 1):
        if primes[i]:
            L = (N - i * i) // i + 1
            primes[i * i:N + 1:i] = [False] * L
    P = [n for (n, prime) in enumerate(primes) if prime]
    return P

def func_2(N, block_size):
    SQRT_N = int(sqrt(N))
    primes = func_1(SQRT_N)
    new_primes = []
    (Nb, r) = divmod(N - SQRT_N, block_size)
    if r > 0:
        Nb += 1
    for ib in range(Nb):
        block = [True] * block_size
        block_beg = SQRT_N + ib * block_size
        for p in primes:
            beg = block_beg % p
            if beg > 0:
                beg = p - beg
            L = (block_size - 1 - beg) // p + 1
            block[beg:block_size:p] = [False] * L
        for k in range(block_size):
            if block[k]:
                n = block_beg + k
                if n <= N:
                    new_primes.append(n)
    primes.extend(new_primes)
    return primes

def func_3(N):
    block_size = 30 * 10 ** 3
    if N <= block_size:
        return func_1(N)
    else:
        return func_2(N, block_size)

def func_4(N):
    NN = N
    P = func_3(int(sqrt(N)))
    D = []
    for p in P:
        (d, r) = divmod(N, p)
        if r == 0:
            D.append(p)
            N = d
        if len(D) > 2:
            break
    if N != NN:
        D.append(N)
    if len(D) == 0:
        return (1, 0)
    elif len(D) == 2:
        return (2, 0)
    else:
        return (1, D[0] * D[1])
N = int(ifs.readline())
(player, move) = func_4(N)
ofs.write('%d\n' % player)
if player == 1:
    ofs.write('%d\n' % move)