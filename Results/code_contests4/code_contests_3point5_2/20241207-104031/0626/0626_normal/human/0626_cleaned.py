sys.setrecursionlimit(20000)
startTime = datetime.now()

def func_1(n):
    return [raw_input().strip() for i in range(n)]

def func_2():
    return raw_input().strip()

def func_3():
    return map(int, func_2().split())

def func_4():
    return func_3()[0]

def func_5(o):
    print(o)

def func_6(a, b):
    while b != 0:
        a %= b
        (a, b) = (b, a)
    return a

def func_7(a, b):
    return a / func_6(a, b) * b

def func_8(node, parent):
    ii = -1
    for i in range(len(node[2])):
        if node[2][i] != parent:
            func_8(node[2][i], node)
        else:
            ii = i
    if ii >= 0:
        node[2].pop(ii)

def func_9(node):
    if node[1] >= 0:
        return
    lcm = 1
    max = -1
    for child in node[2]:
        func_9(child)
        lcm = func_7(lcm, child[0])
    for child in node[2]:
        t = child[1] / lcm * lcm
        if max < 0 or max > t:
            max = t
    node[0] = lcm
    node[1] = max * len(node[2])
n = func_4()
sum = 0
ar = [0] * n
xx = func_3()
for i in range(len(xx)):
    x = xx[i]
    if x == 0:
        ar[i] = [1, -1, []]
    else:
        ar[i] = [1, x, []]
    sum += x
for i in range(n - 1):
    (x, y) = func_3()
    x -= 1
    y -= 1
    ar[x][2].append(ar[y])
    ar[y][2].append(ar[x])
func_8(ar[0], [])
func_9(ar[0])
func_5(sum - ar[0][1])