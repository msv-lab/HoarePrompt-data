def func_1(A, B, C):
    return 2 * (A + 1) * (B + C + 2) + B * C
n = eval(sys.stdin.readline().strip('\n\r ').split()[0])
if n == 1:
    print('17 17')
    exit(0)
r = int(math.sqrt(float(n))) + 1
r3 = int(10 ** (math.log10(float(n)) / 3)) - 1
mx = 8 * n + 9
mn = mx
while r > 0:
    if n % r == 0:
        A = r
        m = n / r
        B = int(math.sqrt(float(m))) + 1
        while B > 0:
            if m % B == 0:
                C = m / B
                mn = min([mn, func_1(A, B, C), func_1(B, A, C), func_1(C, B, A)])
            B -= 1
    r -= 1
print('%d %d' % (mn, mx))