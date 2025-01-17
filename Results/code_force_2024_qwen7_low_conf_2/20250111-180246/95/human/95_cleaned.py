input = sys.stdin.read
data = input().split()

def func_1(a, b):
    while b:
        (a, b) = (b, a % b)
    return a

def func_2():
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        x = int(data[index + 1])
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n
        a.sort()
        gcd1 = func_1(a[-1], a[-2])
        and1 = reduce(lambda x, y: x & y, a[:-2])
        if gcd1 > and1 + x:
            results.append('YES')
            results.append(f'2 {a[-1]} {a[-2]}')
            results.append(f'{n - 2} ' + ' '.join(map(str, a[:-2])))
            continue
        gcd2 = reduce(gcd, a[2:])
        and2 = a[0] & a[1]
        if gcd2 > and2 + x:
            results.append('YES')
            results.append(f'{n - 2} ' + ' '.join(map(str, a[2:])))
            results.append(f'2 {a[0]} {a[1]}')
            continue
        results.append('NO')
    sys.stdout.write('\n'.join(results) + '\n')
func_2()