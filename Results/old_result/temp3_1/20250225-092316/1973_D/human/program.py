T = int(input())
for _ in range(0, T):
    (n, k) = map(int, input().split())
    mx = 1
    while True:
        print(f'? 1 {n * mx}')
        x = int(input())
        if x == n:
            break
        mx += 1
    tar = n // k * mx
    while tar > 0:
        if func_1(tar, k, n):
            break
        tar -= mx
    if tar <= 0:
        print('! -1')
    else:
        print(f'! {tar}')
    x = int(input())
    if x == -1:
        exit(0)

def func_1(tar, k, n):
    it = 0
    ind = 0
    while ind < n and it < k:
        print(f'? {ind + 1} {tar}')
        x = int(input())
        if x == n + 1:
            return False
        ind = x
        it += 1
    return ind == n and it == k

