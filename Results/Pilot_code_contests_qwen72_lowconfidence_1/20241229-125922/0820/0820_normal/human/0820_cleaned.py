try:
    inp = raw_input
except:
    inp = input

def func_1(s):
    sys.stderr.write('{}\n'.format(s))

def func_2():
    return int(inp())

def func_3():
    return [int(_) for _ in inp().split()]
T = func_2()

def func_4(ch):
    return '1' if ch == '0' else '0'

def func_5(a, flips):
    if flips % 2 == 0:
        return a[0]
    else:
        return func_4(a[-1])

def func_6(a, flips):
    if flips % 2 == 0:
        return a[-1]
    else:
        return func_4(a[0])

def func_7(a, b):
    a = deque(a)
    out = []
    flips = 0
    for i in range(len(a) - 1, -1, -1):
        if func_6(a, flips) == b[i]:
            if flips % 2 == 0:
                a.pop()
            else:
                a.popleft()
            continue
        if func_5(a, flips) != b[i]:
            out.append(i + 1)
        else:
            out.append(1)
            out.append(i + 1)
        flips += 1
        if flips % 2 == 0:
            a.pop()
        else:
            a.popleft()
    return out
for _ in range(T):
    N = func_2()
    a = list(inp())
    b = list(inp())
    out = func_7(a, b)
    print(' '.join(map(str, [len(out)] + out)))