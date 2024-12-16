(n, k) = map(int, input().split())
if n < k:
    print('No')
else:
    a = []
    i = 0
    while n > 0:
        x = n.bit_length() - 1
        if x <= i:
            break
        a.append(x)
        n -= 2 ** x
        i += 1
    if len(a) < k:
        print('No')
    else:
        a = a[:k]
        a.sort(reverse=True)
        print('Yes')
        print(' '.join(map(str, a)))