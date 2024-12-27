def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


n = int(raw_input())
seq = [int(x) for x in raw_input().split()]


seq.sort(reverse=True)

elems = [seq[0]]
gcds = {}
for elem in seq:
    gcds[elem] = 0

i = 1
j = 1
while i < n:
    if gcds[seq[j]] != 0:
        gcds[seq[j]] -= 1
        j += 2
    else:
        l = len(elems)
        for k in xrange(l):
            gcds[gcd(elems[k], seq[j])] += 1

        elems.append(seq[j])
        j += 1
        i += 1



print(' '.join([str(x) for x in elems]))



