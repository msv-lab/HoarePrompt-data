mod = pow(10, 9) + 7
e = pow(10, -6)
input = lambda : sys.stdin.readline().rstrip('\r\n')
N = pow(10, 6)

def func_1():
    return map(int, input().split())

def func_2():
    return list(map(int, input().split()))

def func_3(n, v):
    return [v for i in range(n)]

def func_4(n, m, v):
    return [[v for i in range(m)] for i in range(n)]

def func_5(n, m):
    l = [[] for i in range(n + 1)]
    for i in range(m):
        (x, y) = func_1()
        l[x].append(y)
        l[y].append(x)
    return l

def func_6(n, m):
    l = [[0 for i in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        (x, y) = func_1()
        l[x][y] = 1
        l[y][x] = 1
    return l

class SegmentTree:

    def init(arr):
        n = len(arr)
        tree = [0] * (2 * n)
        for i in range(n):
            tree[n + i] = arr[i]
        for i in range(n - 1, -1, -1):
            tree[i] = tree[i << 1] + tree[i << 1 | 1]
        return tree

    def add(tree, i, v):
        i += len(tree) // 2
        tree[i] = v
        while i > 1:
            tree[i >> 1] = tree[i] + tree[i ^ 1]
            i >>= 1

    def range_sum(tree, l, r):
        l += len(tree) // 2
        r += len(tree) // 2
        sum = 0
        while l < r:
            if l & 1:
                sum += tree[l]
                l += 1
            if r & 1:
                r -= 1
                sum += tree[r]
            l >>= 1
            r >>= 1
        return sum

def func_7(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
    return d

def func_8(l):
    n = len(l)
    m = len(l[0])
    p = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            p[i][j] = p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]
    return p

def func_9(x):
    return max(1 - (x & x - 1), 0)

def func_10(l):
    a = 0
    for i in l:
        a = gcd(a, i)
    return a

def func_11(num):
    prime = [True for i in range(num + 1)]
    Highest_Prime = [0 for i in range(num + 1)]
    Lowest_Prime = [0 for i in range(num + 1)]
    prime[0] = prime[1] = False
    p = 2
    while p <= num:
        if prime[p] == True:
            Lowest_Prime[p] = p
            Highest_Prime[p] = p
            for i in range(2 * p, num + 1, p):
                prime[i] = False
                Highest_Prime[i] = p
                if Lowest_Prime[i] == 0:
                    Lowest_Prime[i] = p
        p += 1
    p = []
    for i in range(num + 1):
        if prime[i]:
            p.append(i)
    return p

def func_12(num, Prime_array):
    d = {}
    while num != 1:
        x = Prime_array[num]
        d[x] = d.get(x, 0) + 1
        num //= x
    return d

def func_13(n):
    d = {}
    x = 2
    while x * x <= n:
        while n % x == 0:
            d[x] = d.get(x, 0) + 1
            n //= x
        x += 1
    if n > 1:
        d[n] = d.get(n, 0) + 1
    return d

def func_14(d):
    s = 0
    for i in d:
        s += pow(i, d[i] - 1) * (i - 1)
    return s

def func_15(n, mod):
    f = [1]
    for i in range(1, n + 1):
        f.append(f[i - 1] * i % mod % mod)
    return f

def func_16(n, mod):
    if mod == -1:
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) * (dearr[i - 1] + dearr[i - 2]))
    else:
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod)
    return dearr

def func_17(p, x):
    i = bisect_left(p, x)
    if i != len(p) and p[i] == x:
        return i
    else:
        return -1

def func_18(p, x):
    n = len(p)
    (l, r) = (0, n - 1)
    if p[0] > x:
        return -1
    while l <= r:
        mid = (l + r) // 2
        if p[mid] <= x:
            if mid != n - 1:
                if p[mid + 1] > x:
                    break
                else:
                    l = mid + 1
            else:
                mid = n - 1
                break
        else:
            r = mid - 1
    return mid

def func_19(p, x):
    n = len(p)
    (l, r) = (0, n - 1)
    if p[-1] < x:
        return n
    while l <= r:
        mid = (l + r) // 2
        if p[mid] >= x:
            if mid != 0:
                if p[mid - 1] < x:
                    break
                else:
                    r = mid - 1
            else:
                mid = 0
                break
        else:
            l = mid + 1
    return mid

def func_20(x):
    if x == 0 or x == 1:
        return x
    l = 1
    r = x
    while l <= r:
        mid = (l + r) / 2
        y = mid * mid
        if y > x:
            r = mid - 1
        elif y == x:
            return mid
        elif (mid + 1) * (mid + 1) > x:
            return mid
        else:
            l = mid + 1

def func_21(a, b, mod):
    ans = 1
    a %= mod
    while b:
        if b & 1:
            ans = ans * a % mod
        a = a * a % mod
        b >>= 1
    return ans

def func_22(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    (i, j) = (len(a), len(b))
    l = []
    while i != 0 and j != 0:
        if dp[i][j] == dp[i][j - 1]:
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            i -= 1
            j -= 1
            l.append(a[i])
    s = ''.join(l)
    return s[::-1]

def func_23(arr):
    l = []
    for i in arr:
        pos = bisect_left(l, i)
        if pos == len(l):
            l.append(i)
        else:
            l[pos] = i
    return len(l)
graph = []
vis = []

def func_24(ver):
    stack = []
    stack.append(ver)
    vis[ver] = 1
    while len(stack):
        ver = stack.pop()
        print(ver, end=' ')
        for node in graph[ver]:
            if not vis[node]:
                stack.append(node)
                vis[node] = 1

def func_25(ver):
    q = deque()
    q.append(ver)
    vis[ver] = 1
    while len(q):
        ver = q.popleft()
        print(ver, end=' ')
        for node in graph[ver]:
            if not vis[node]:
                q.append(node)
                vis[node] = 1
for _ in range(int(input())):
    (n, x, y) = map(int, input().split())
    ans = x - 2
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(1, x):
        if arr[i - 1] + 2 == arr[i]:
            ans += 1
    if arr[x - 1] == n - 1 and arr[0] == 1:
        ans += 1
    if arr[x - 1] == n and arr[0] == 2:
        ans += 1
    print(ans)