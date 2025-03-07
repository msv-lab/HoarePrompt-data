def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        s = sys.stdin.readline().strip()
        cases.append((n, s))
    return cases

def func_2(case):
    ups = sum((1 for c in case[1] if c == 'U'))
    return 'YES' if ups % 2 else 'NO'
cases = func_1()
for case in cases:
    print(func_2(case))