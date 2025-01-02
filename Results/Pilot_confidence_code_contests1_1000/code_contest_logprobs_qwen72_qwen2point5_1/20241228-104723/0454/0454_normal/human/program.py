def main(data):
    n, k = map(int, data.split())
    result = [0]
    n -= 1
    k -= 1
    cur_delta = 0
    while k < n and n > 0:
        result.append(result[-1] + 1)
        n -= 1
        cur_delta += 1
    while n > 0:
        if cur_delta > 0:
            cur_delta = -(cur_delta + 1)
        else:
            cur_delta = -(cur_delta - 1)
        result.append(result[-1] + cur_delta)
        n -= 1
    m = min(result)
    for r in result:
        print (r-m)+1,

import sys
main(sys.stdin.readline())
