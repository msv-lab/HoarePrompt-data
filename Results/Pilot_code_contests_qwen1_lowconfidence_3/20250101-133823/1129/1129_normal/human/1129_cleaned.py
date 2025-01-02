def func_1(s):
    return [int(x) for x in s.split()]

def func_2(args):
    a_s = tuple(func_1(args[1]))
    return a_s

def func_3(args, verbose=False):
    a_s = func_2(args)
    max_1 = -float('inf')
    min_2 = float('inf')
    for k in xrange(len(a_s) - 1):
        max_1 = max(max_1, a_s[k + 1] - a_s[k])
    for k in xrange(len(a_s) - 2):
        min_2 = min(min_2, a_s[k + 2] - a_s[k])
    return max(max_1, min_2)

def func_4():
    assert func_1('1 2 3') == [1, 2, 3]
    assert func_3(['3', '1 4 6']) == 5
    assert func_3(['5', '1 2 3 4 5']) == 2
    assert func_3(['5', '1 2 3 7 8']) == 4
if __name__ == '__main__':
    from sys import argv
    if argv.pop() == 'test':
        func_4()
    else:
        func_3(list(fileinput.input()), verbose=True)