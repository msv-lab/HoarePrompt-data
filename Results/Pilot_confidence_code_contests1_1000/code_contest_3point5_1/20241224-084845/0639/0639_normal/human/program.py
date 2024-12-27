def isPrime(x):
    i = 2
    while i * i <= x:
        if x % i == 0: return 0
        i += 1
    return 1
def solve(x, k):
    def dfs(dep, n, p, x):
        if (dep == len(v) or v[dep] * p > x):
            return - (x // p) * (n % 2 * 2 - 1)
        return dfs(dep + 1, n, p, x) + dfs(dep + 1, n + 1, v[dep] * p, x)
    if k <= 5000:
        v = [i for i in range(2, k)]
        return dfs(0, 0, 1, x // k)
    else:
        r, last, i = 0, x // k, i
        v = [0] * (last + 1)
        while i * i <= last:
            if (v[i] == 0):
                c = i
                while c <= last:
                    if (v[c] == 0): v[c] = i
                    c += i
            i += 1
        for i in range(1, last + 1):
            r += i == 1 or (v[i] == 0 and i >= k) or v[i] >= k
        return r
a,b,k = raw_input().split(" ")
k = int(k)
if not isPrime(k):
    print(0)
else:
    print(solve(int(b), k) - solve(int(a) - 1, k))
