(a, b, m) = map(int, raw_input().split())
for i in range(1, min(a + 1, m + 1)):
    if (m - i * 10 ** 9 % m) % m > b:
        print(1, '%(x)09d' % {'x': i})
        sys.exit()
print(2)