def func_1(a):
    return [-v for v in a]

def func_2(s):
    assert len(s) > 0
    pre_s = s[:-1]
    v = s[-1]
    if len(pre_s) == 0:
        return [v]
    return func_2(pre_s) + [v] + func_1(func_2(pre_s)) + [-v]

def func_3(v):
    if v > 0:
        return [(i, 0) for i in range(1, v + 1)] + [(v, 1), (v - 1, 1)] + [(i, 0) for i in range(v - 1, 0, -1)]
    elif v < 0:
        return func_3(-v)[::-1]
    assert False

def func_4(v):
    return func_3(v) + [(0, 0)]

def func_5():
    func_6('1', '11')

def func_6(s1, s2):
    ok = True
    n = int(s1)
    ret_gp = []
    for i in range(2 ** n - 1, -1, -1):
        s = [v + 1 for v in range(n) if (i >> v) % 2 == 1]
        if s2[i] == '0':
            for ind in range(n):
                if (i >> ind) % 2 == 0 and s2[i + 2 ** ind] == '1':
                    ok = False
            ret_gp += func_2(s)
    ret_path = [(0, 0)] + [p for v in ret_gp for p in func_4(v)]
    if ok:
        print('Possible')
        print(len(ret_path) - 1)
        for (x, y) in ret_path:
            print(str(x) + ' ' + str(y))
    else:
        print('Impossible')
s1 = raw_input()
s2 = raw_input()
func_6(s1, s2)