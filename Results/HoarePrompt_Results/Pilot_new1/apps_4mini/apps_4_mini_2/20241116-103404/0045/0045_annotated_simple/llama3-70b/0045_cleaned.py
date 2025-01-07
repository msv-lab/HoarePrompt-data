def func_1(a, b):
    while b:
        (a, b) = (b, a % b)
    return a
(n, k) = map(int, input().split())
if n < k:
    print(-1)
else:
    seq = []
    for i in range(1, k + 1):
        if n >= i:
            seq.append(i)
            n -= i
        else:
            break
    if len(seq) != k:
        print(-1)
    else:
        print(' '.join(map(str, seq)))