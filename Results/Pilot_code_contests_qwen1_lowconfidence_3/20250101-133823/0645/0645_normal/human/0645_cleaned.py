inp = raw_input

def func_1(s):
    sys.stderr.write('{}\n'.format(s))

def func_2():
    return int(inp())

def func_3():
    return [int(_) for _ in inp().split()]
N = func_2()
A = func_3()
out = [0] * N
fail = False
B = []
for i in range(N - 1, -1, -1):
    j = i + 1
    S = 0
    for k in range(i, N, j):
        S += out[k]
    if S % 2 != A[i]:
        out[i] = 1
        B.append(j)
print(len(B))
if len(B):
    print(' '.join(map(str, B)))