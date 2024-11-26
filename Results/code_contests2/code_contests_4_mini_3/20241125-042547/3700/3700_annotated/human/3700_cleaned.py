mod = 1000000000.0 + 7

def func_1(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def func_2():
    (H, N) = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if s >= H:
        print('Yes')
    else:
        print('No')
func_2()