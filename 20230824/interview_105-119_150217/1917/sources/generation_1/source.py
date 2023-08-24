def choose_projects(n, k, a):
    b = [0] * n
    remaining_projects = k
    for i in range(n):
        b[i] = min(a[i], remaining_projects)
        remaining_projects -= b[i]
    return b

n, k = map(int, input().split())
a = list(map(int, input().split()))

b = choose_projects(n, k, a)
print(*b)