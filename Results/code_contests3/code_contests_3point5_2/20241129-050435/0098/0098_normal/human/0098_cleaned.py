def func_1(n):
    return math.cos(math.pi / (4 * n)) / math.sin(math.pi / (2 * n))
for ca in xrange(int(raw_input())):
    n = int(raw_input())
    print('%.9f' % func_1(n))