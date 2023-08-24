def choose_projects(n, k, a):
    b = [0] * n
    remaining_projects = k
    f_value = 0

    # Sort project types based on completed projects
    project_types = list(enumerate(a))
    project_types.sort(key=lambda x: x[1], reverse=True)

    for i in range(n-1, -1, -1):
        project_index = project_types[i][0]
        b[i] = min(a[project_index], remaining_projects)
        remaining_projects -= b[i]
        f_value += b[i] * (a[project_index] - b[i]**2)

    return b, f_value

n, k = map(int, input().split())
a = list(map(int, input().split()))

b, f_value = choose_projects(n, k, a)
print(*b)