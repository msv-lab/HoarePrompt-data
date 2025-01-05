setrecursionlimit(2 * 10 ** 5)

def func_1():
    return map(long, stdin.readline().split())

def func_2(li):
    if not li:
        return
    for i in xrange(len(li) - 1):
        stdout.write('%d ' % li[i])
    stdout.write('%d\n' % li[-1])

def func_3():
    return stdin.readline().rstrip()
n = int(func_3())
li = func_1()
N = max(li)
done = [0] * (N + 1)
nos = [0] * (N + 1)
primCount = [0] * (N + 1)
for i in li:
    nos[i] += 1
for i in xrange(2, N + 1):
    if done[i] == 0:
        for j in xrange(i, N + 1, i):
            done[j] = 1
            if nos[j]:
                primCount[i] += nos[j]
for i in xrange(1, N + 1):
    primCount[i] += primCount[i - 1]
m = int(func_3())
for i in xrange(m):
    (l, r) = func_1()
    if r > N:
        r = N
    if l > N:
        l = N + 1
    stdout.write('%d\n' % (primCount[r] - primCount[l - 1]))