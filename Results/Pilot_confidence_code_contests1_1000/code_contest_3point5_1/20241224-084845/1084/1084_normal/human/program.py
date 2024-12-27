#!/usr/bin/env python3

from __future__ import division, print_function

def solver(ifs):
    n, m = list(map(int, ifs.readline().split()))
    used = []
    unused = []
    for i, _ in enumerate(range(m)):
        a, b = list(map(int, ifs.readline().split()))
        if b == 1:
            used.append( (a, i) )
        else:
            unused.append( (a, i) )
    used.sort()
    unused.sort()
    res = [None, ] * m
    for i, (w, pos) in enumerate(used):
        res[pos] = (i, i+1)
    ref = 2
    counter = 0
    for w, pos in unused:
        if ref >= n:
            print(-1)
            return None
        if w >= used[ref-1][1]:
            res[pos] = (counter, ref)
            counter += 1
        else:
            print(-1)
            return None
        if counter >= ref-1:
            ref += 1
            counter = 0
    print("\n".join("%d %d" % (u+1, v+1) for u, v in res))
    return None

def main():
    import sys
    if sys.version_info.major == 3:
        from io import StringIO as StreamIO
    else:
         from io import BytesIO as StreamIO
    
    with StreamIO(sys.stdin.read()) as ifs, StreamIO() as ofs:
        _stdout = sys.stdout
        sys.stdout = ofs
        solver(ifs)
        sys.stdout = _stdout
        sys.stdout.write(ofs.getvalue())
    return 0

if __name__ == '__main__':
    main()
