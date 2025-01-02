import sys

inp = [map(int, i.split(' ')) for i in sys.stdin.read().splitlines()]

n, L, R, QL, QR = inp[0]
w = inp[1]

def test(f):
    global L, R, QL, QR, w
    ret = 0
    l, r = 0, len(w)
    action = None
    while l != r:
        cost_l = w[l  ]*L + (QL if action == 0 else 0)
        cost_r = w[r-1]*R + (QR if action == 1 else 0)
        if action is not None:
            if cost_l < cost_r:
                action = 0
            elif cost_l > cost_r:
                action = 1
        else:
            action = f
        if action == 0:
            ret += cost_l
            l += 1
        else:
            ret += cost_r
            r -= 1
    return ret

res = min(test(0), test(1))

sys.stdout.write(str(res))
