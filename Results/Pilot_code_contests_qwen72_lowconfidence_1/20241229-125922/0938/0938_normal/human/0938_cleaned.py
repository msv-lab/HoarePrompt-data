(N, K) = map(int, raw_input().split())
A = sorted(list(map(int, raw_input().split())))
if K > A[-1]:
    print('IMPOSSIBLE')
else:
    flag = True
    tmp = reduce(gcd, A)
    if tmp != 1:
        flag = False
    for a in A:
        if a == K or (K - a) % tmp == 0:
            flag = True
            break
    if flag:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')