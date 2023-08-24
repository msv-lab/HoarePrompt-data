def power(a, n, p):
    res = a
    while n > 0:
        if n & 1:
            res = (res * a) % p
        a = (a * a) % p
        n = n >> 1
    return res

def count_functions(p, k):
    if k == 0:
        return 1
    elif k == 1:
        return p
    else:
        visited = [False] * p
        cycle_count = 0
        for i in range(p):
            if visited[i]:
                continue
            x = i
            while not visited[x]:
                visited[x] = True
                x = (k * x) % p
            cycle_count += 1
        return power(p, cycle_count, 1000000007)

p, k = map(int, input().split())
num_functions = count_functions(p, k)
print(num_functions)