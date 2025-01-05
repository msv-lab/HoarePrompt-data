#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin, exit


def main():
    ans = [0] * 4001
    for line in stdin:
        n = int(line)

        if not ans[n]:
            count = 0
            for a in xrange((n if n < 1000 else 1000) + 1):
                e1 = n-a-1001 if n-a-1001 >= 0 else -1
                for nab in xrange(n-a, e1, -1):
                    ran = ((nab if nab < 1000 else 1000) -
                           ((nab-1001) if nab > 1000 else -1))
                    if ran >= 0:
                        count += ran

            ans[n] = count
        print(ans[n])
    exit()


if __name__ == '__main__':
    main()