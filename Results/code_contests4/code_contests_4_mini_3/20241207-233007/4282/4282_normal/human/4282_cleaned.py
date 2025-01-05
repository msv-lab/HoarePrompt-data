class macro:

    def __init__(self, level):
        self.level = level

    def __add__(self, other):
        return macro('+0'[self.level == '0' or other.level == '0'])

    def __sub__(self, other):
        return macro('+0'[self.level == '0' or other.level in '0+'])

    def __mul__(self, other):
        return macro('*0'[self.level in '0+' or other.level in '0+'])

    def __div__(self, other):
        return macro('*0'[self.level in '0+' or other.level in '0+*'])

def func_1(c):
    return 'macro("' + c + '")'

def func_2(s):
    (f, n) = ([''], '')
    for c in ''.join(s):
        if c in '+-*/()':
            if n != '':
                f[-1] += func_1(v.get(n, '1'))
                n = ''
            if c == '(':
                f.append('')
            elif c == ')':
                m = func_1('10'[eval(f.pop()).level == '0'])
                f[-1] += m
            else:
                f[-1] += c
        else:
            n += c
    if n != '':
        f[0] += func_1(v.get(n, '1'))
    return eval(f[0]).level
v = {}
for i in xrange(input()):
    s = raw_input().split()
    if s[0] == '#':
        s.pop(0)
    v[s[1]] = func_2(s[2:])
print['OK', 'Suspicious'][func_2(raw_input().split()) == '0']