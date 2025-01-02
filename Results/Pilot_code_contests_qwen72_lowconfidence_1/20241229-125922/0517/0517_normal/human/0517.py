N = int(raw_input())
a = [int(x)-1 for x in raw_input().split()]
weight = [1] * N
M = 10**9+7
def factorial(n):
    acc = 1
    for i in xrange(1, 1 + n):
        acc = (acc * i) % M
    return acc
def inv(n):
    return pow(n, M-2, M)
for i in xrange(N-1):
    weight[N-2-i] = (weight[N-1-i] * (i+1)) % M
missing = list(set(xrange(N)) - set(a))
missing.sort()
n_missing = len(missing)
sum_missing = sum(missing)
avg_missing = sum_missing * inv(n_missing)
n_present = N - n_missing
n_rows = factorial(n_missing)
acc = 0
i_missing = 0
i_present = 0
missing_lt_tot = 0
for i, (w, x) in enumerate(zip(weight, a)):
    if x == -1:
        ai = avg_missing
        bi = i_missing * inv(2) + i_present - missing_lt_tot * inv(n_missing)
        i_missing += 1
    else:
        ai = x
        bi = 0
        for j in xrange(i):
            if a[j] != -1 and a[j] < a[i]:
                bi += 1
        missing_lt = 0
        for j in missing:
            if j < a[i]:
                missing_lt += 1
        missing_lt_tot += missing_lt
        #print '@', missing_lt, n_missing, i_missing, n_rows
        bi += missing_lt * inv(n_missing) * i_missing
        coeff = 1
        i_present += 1
    #print (ai * n_rows) % M, (bi * n_rows) % M, w
    acc = (acc + ((ai - bi) * n_rows) * w) % M
print (acc + n_rows) % M
