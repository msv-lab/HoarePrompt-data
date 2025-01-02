base = int(sys.stdin.readline())

def func_1(num, b, numerals='0123456789'):
    return num == 0 and '0' or func_1(num // b, b).lstrip('0') + numerals[num % b]
for i in range(1, base):
    for j in range(1, base):
        if j != 1:
            sys.stdout.write(' ')
        n = i * j
        if base != 10:
            n = int(func_1(n, base))
        sys.stdout.write('%d' % n)
    sys.stdout.write('\n')