from sys import stdin

n, a = int(input()), set([int(x) for x in stdin.readline().split()])
out, Max, ix = [], 1000000, 1
y = set([i for i in range(1, Max + 1) if i not in a])

while a:
    ele = a.pop()
    sym = Max - ele + 1
    if sym not in a:
        out.append(sym)
    else:
        a.discard(sym)
        while ix <= Max:
            sym = Max - ix + 1
            if ix in y and sym in y:
                y.discard(sym)
                y.discard(ix)
                out.extend([ix, sym])
                break
            ix += 1

print('%d\n%s' % (len(out), ' '.join(map(str, out))))
