line = raw_input()
(n, m) = line.split()
n = int(n)
m = int(m)
line = raw_input()
nr_minus = line.count('-')
minimum = min(nr_minus, n - nr_minus)
for i in xrange(m):
    line = raw_input()
    (l, r) = line.split()
    l = int(l)
    r = int(r)
    length = r - l + 1
    if length % 2 == 0:
        length = length / 2
        if length <= minimum:
            print(1)
        else:
            print(0)
    else:
        print(0)