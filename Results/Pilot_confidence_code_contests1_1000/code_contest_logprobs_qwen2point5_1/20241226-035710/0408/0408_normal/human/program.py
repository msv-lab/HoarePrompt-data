def incr(a, k):
    carry = 1
    for i in range(len(a) - 1, -1, -1):
        newval = a[i] + carry
        if newval >= k:
            if i == 0:
                return False
            newval = 0
            carry = 1
        else:
            carry = 0
        a[i] = newval
    return True
def sol():
    n, k, d = map(int, raw_input().split())
    a = [0] * d
    res = list()
    nextFine = True
    for want in xrange(n):
        if not nextFine:
            print(-1)
            return
        res.append(list(val + 1 for val in a))
        nextFine = incr(a, k)
    print('\n'.join(' '.join(map(str, l)) for l in res))
sol()