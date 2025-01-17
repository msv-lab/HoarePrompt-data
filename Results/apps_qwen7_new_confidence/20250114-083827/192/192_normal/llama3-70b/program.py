def inverse_modulo(p, mod):
    return pow(p, -1, mod)

def count_inversions(a):
    n = len(a)
    inversions = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                inversions += 1
    return inversions

n, k = map(int, input().split())
a = list(map(int, input().split()))

inversions = count_inversions(a)
if inversions % 2 == k % 2:
    P = 1
    Q = 1
    for i in range(1, n):
        if a[i-1] > a[i]:
            Q *= i
            Q %= 10**9 + 7
    if Q == 0:
        print(0)
    else:
        print(P * inverse_modulo(Q, 10**9 + 7) % (10**9 + 7))
else:
    print(0)
