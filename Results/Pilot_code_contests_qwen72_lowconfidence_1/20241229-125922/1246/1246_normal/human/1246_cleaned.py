(fin, fout) = (sys.stdin, sys.stdout)
MOD = 2 ** 15
make_op = lambda op: lambda s, o: Num(op(s.x, o.x) % MOD)
make_cmp = lambda op: lambda s, o: op(s.x, o.x)

class Num:

    def __init__(self, obj):
        self.x = obj.x if isinstance(obj, Num) else int(obj)
    __add__ = make_op(op.add)
    __sub__ = make_op(op.sub)
    __div__ = make_op(op.div)
    __mul__ = make_op(op.mul)
    __eq__ = make_cmp(op.eq)
    __lt__ = make_cmp(op.lt)
    __gt__ = make_cmp(op.gt)

def func_1(num):
    return num.x if isinstance(num, Num) else num
n = int(fin.readline())
text = ''.join(fin.readlines())
for (pat, repl) in [('\\s', ''), ('return', 'return '), ('.*{(.*)}.*', '\\1'), ('(\\d+)', 'Num(\\1)'), ('(if.*?)(return)', '\\1:\\2'), (';', '\n\t')]:
    text = re.sub(pat, repl, text)
text = 'def F(n):\n\tn = Num(n)\n\t' + text
exec(compile(text.strip(), 'f**k', 'exec'))
cache = {}
f = lambda n: Num(cache[func_1(n)])
ans = -1
for i in range(0, MOD):
    t = cache[i] = Num(F(i))
    if func_1(t) == n:
        ans = i
print(ans)